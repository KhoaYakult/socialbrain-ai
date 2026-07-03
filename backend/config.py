"""
Quản lý cấu hình ứng dụng.

Module này sử dụng pydantic-settings để:
1. Đọc biến môi trường từ file .env
2. Validate giá trị (đúng kiểu dữ liệu, không thiếu)
3. Cung cấp 1 object `settings` duy nhất cho toàn bộ app

Tại sao dùng pydantic-settings thay vì os.getenv()?
- os.getenv("PORT") trả về string "8000" → phải tự convert int()
- Nếu thiếu biến → os.getenv trả None → lỗi runtime khó debug
- pydantic-settings tự convert kiểu, báo lỗi rõ ràng khi thiếu biến
"""

from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Cấu hình toàn cục của ứng dụng.

    Mỗi field tương ứng với 1 biến môi trường trong file .env.
    Pydantic tự động:
    - Đọc giá trị từ .env
    - Convert sang đúng kiểu (str → int, str → bool)
    - Báo lỗi nếu thiếu biến bắt buộc (không có default)
    """

    # --- Thông tin App ---
    # Field có giá trị mặc định → KHÔNG bắt buộc trong .env
    app_name: str = "SocialBrain AI"
    app_version: str = "0.1.0"
    app_env: str = "development"  # development | staging | production
    debug: bool = True

    # --- Server ---
    host: str = "127.0.0.1"
    port: int = 8000  # pydantic tự convert string "8000" → int 8000

    # --- LLM API Keys ---
    # Giá trị mặc định = chuỗi rỗng → app vẫn khởi động được
    # nhưng sẽ báo lỗi khi thực sự gọi API ở Phase 1
    gemini_api_key: str = ""
    openai_api_key: str = ""

    # --- Ollama (Phase 6) ---
    ollama_base_url: str = "http://localhost:11434"

    # Cấu hình cho pydantic-settings: đọc từ file .env nào
    model_config = SettingsConfigDict(
        env_file=".env",          # Tên file chứa biến môi trường
        env_file_encoding="utf-8",  # Encoding của file .env
        case_sensitive=False,     # APP_NAME hay app_name đều match
        extra="ignore",           # Bỏ qua biến lạ trong .env (không báo lỗi)
    )


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """
    Factory function trả về Settings singleton.

    Tại sao dùng @lru_cache?
    - Settings chỉ cần đọc file .env MỘT LẦN khi app khởi động
    - Các lần gọi sau trả về object đã cache → nhanh, tiết kiệm I/O
    - maxsize=1 vì chỉ cần cache đúng 1 instance

    Tại sao dùng function thay vì biến global?
    - Dễ override trong tests: mock get_settings() → trả Settings khác
    - Lazy loading: chỉ đọc .env khi thực sự cần, không phải lúc import
    """
    return Settings()


# Tạo instance mặc định để import nhanh
# Cách dùng: from backend.config import settings
settings = get_settings()
