"""
SocialBrain AI — Entry Point.

Đây là file khởi động chính của ứng dụng.
Khi chạy `uvicorn backend.main:app --reload`, uvicorn sẽ:
1. Import module này
2. Tìm biến `app` (FastAPI instance)
3. Khởi động HTTP server và lắng nghe request

File này chỉ làm 3 việc:
- Tạo FastAPI app
- Đăng ký các router (API endpoints)
- Định nghĩa lifecycle events (startup/shutdown)
"""

from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from backend.config import settings
from backend.utils.logger import logger


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """
    Quản lý lifecycle (vòng đời) của ứng dụng.

    asynccontextmanager chia thành 2 phần bởi `yield`:
    - TRƯỚC yield: Code chạy KHI APP KHỞI ĐỘNG (startup)
    - SAU yield: Code chạy KHI APP TẮT (shutdown)

    Tại sao cần lifecycle?
    - Startup: khởi tạo database connection, load AI model, warmup cache
    - Shutdown: đóng connection, giải phóng tài nguyên, flush logs

    AsyncGenerator[None, None]:
    - Generic type cho async generator
    - [YieldType, SendType] = [None, None] vì ta không trả/nhận giá trị
    """
    # ===== STARTUP =====
    logger.info(f"🚀 Khởi động {settings.app_name} v{settings.app_version}")
    logger.info(f"📍 Môi trường: {settings.app_env}")
    logger.info(f"🔧 Debug mode: {settings.debug}")
    logger.info(f"🌐 Server: http://{settings.host}:{settings.port}")

    # Placeholder: Khởi tạo services sẽ thêm ở các Phase sau
    # Phase 1: Khởi tạo LLM Gateway
    # Phase 3: Khởi tạo ChromaDB connection
    # Phase 4: Khởi tạo Database + Scheduler

    yield  # ← App đang chạy, phục vụ request tại đây

    # ===== SHUTDOWN =====
    logger.info("👋 Đang tắt server...")
    # Placeholder: Cleanup sẽ thêm ở các Phase sau
    # Phase 3: Đóng ChromaDB connection
    # Phase 4: Dừng scheduler, đóng database
    logger.info("✅ Server đã tắt sạch sẽ.")


# ============================================================
# Tạo FastAPI Application
# ============================================================
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description=(
        "AI-powered Social Media Manager — "
        "Tạo nội dung, lên lịch đăng bài, phân tích engagement tự động."
    ),
    lifespan=lifespan,
    # Tự động tạo trang docs tại /docs (Swagger UI)
    docs_url="/docs" if settings.debug else None,
    # Tự động tạo trang docs tại /redoc (ReDoc — giao diện khác)
    redoc_url="/redoc" if settings.debug else None,
)


# ============================================================
# CORS Middleware
# ============================================================
# CORS = Cross-Origin Resource Sharing
# Khi frontend (localhost:5500) gọi API backend (localhost:8000)
# → trình duyệt chặn vì "khác origin" (khác port = khác origin)
# → Middleware này cho phép frontend gọi API
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5500",     # VS Code Live Server
        "http://127.0.0.1:5500",
        "http://localhost:3000",     # Nếu dùng frontend framework
        "http://127.0.0.1:8000",    # Chính server API
    ],
    allow_credentials=True,          # Cho phép gửi cookies
    allow_methods=["*"],             # Cho phép mọi HTTP method (GET, POST, PUT, DELETE)
    allow_headers=["*"],             # Cho phép mọi header
)


# ============================================================
# Đăng ký Routers (API Endpoints)
# ============================================================
# Sẽ thêm dần ở các Phase:
# Phase 1: app.include_router(chat_router, prefix="/api")
# Phase 2: app.include_router(content_router, prefix="/api")
# Phase 3: app.include_router(knowledge_router, prefix="/api")
# Phase 4: app.include_router(calendar_router, prefix="/api")


# ============================================================
# Health Check Endpoint
# ============================================================
@app.get(
    "/",
    summary="Health Check",
    description="Kiểm tra server đang hoạt động. Trả về thông tin cơ bản.",
    tags=["System"],
)
async def health_check() -> dict[str, str]:
    """
    Endpoint đơn giản nhất — xác nhận server sống.

    Tại sao cần health check?
    - Monitoring tools (UptimeRobot, AWS) gọi định kỳ để kiểm tra
    - CI/CD pipeline kiểm tra sau khi deploy
    - Developer kiểm tra nhanh: curl http://localhost:8000/

    Returns:
        dict: Thông tin app gồm tên, version, trạng thái.
    """
    return {
        "app": settings.app_name,
        "version": settings.app_version,
        "status": "running",
        "environment": settings.app_env,
    }


@app.get(
    "/api/health",
    summary="API Health Check",
    description="Kiểm tra API layer hoạt động bình thường.",
    tags=["System"],
)
async def api_health() -> dict[str, str]:
    """
    Health check cho API layer.

    Tách riêng với root "/" vì:
    - "/" có thể bị frontend chiếm (serve index.html)
    - "/api/health" luôn thuộc về backend
    """
    return {
        "status": "healthy",
        "api_version": "v1",
    }
