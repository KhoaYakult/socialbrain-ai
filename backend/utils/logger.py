"""
Cấu hình logging cho toàn bộ ứng dụng.

Tại sao cần logging thay vì print()?
1. print() → chỉ hiện ra terminal, không ghi file, không có timestamp
2. logging → có mức độ (DEBUG/INFO/WARNING/ERROR), có timestamp,
   có thể ghi ra file, có thể tắt/bật theo mức
3. Trong production: tắt DEBUG, chỉ giữ WARNING trở lên

Dự án này dùng thư viện `rich` để logging ra terminal đẹp hơn,
có màu sắc, dễ phân biệt mức độ log.
"""

import logging
import sys
from typing import Optional

from rich.console import Console
from rich.logging import RichHandler


def setup_logger(
    name: str = "socialbrain",
    level: int = logging.DEBUG,
    log_file: Optional[str] = None,
) -> logging.Logger:
    """
    Tạo và cấu hình logger cho ứng dụng.

    Args:
        name: Tên logger. Dùng tên dự án để phân biệt với log
              của thư viện khác (uvicorn, fastapi...).
        level: Mức log tối thiểu sẽ hiển thị.
               DEBUG=10 < INFO=20 < WARNING=30 < ERROR=40 < CRITICAL=50
               Ví dụ: level=WARNING → chỉ hiện WARNING, ERROR, CRITICAL.
        log_file: Đường dẫn file log (tùy chọn).
                  Nếu None → chỉ log ra terminal.

    Returns:
        logging.Logger: Logger đã được cấu hình, sẵn sàng sử dụng.

    Cách dùng:
        from backend.utils.logger import setup_logger
        logger = setup_logger()
        logger.info("Server đã khởi động")
        logger.error("Không kết nối được database")
    """
    # Tạo logger với tên cho trước
    # Nếu logger cùng tên đã tồn tại → trả về cái cũ (Python caching)
    logger = logging.getLogger(name)

    # Đặt mức log tối thiểu
    logger.setLevel(level)

    # Xóa handler cũ (tránh duplicate log khi gọi setup_logger nhiều lần)
    logger.handlers.clear()

    # === Handler 1: Terminal (dùng Rich để có màu) ===
    console_handler = RichHandler(
        console=Console(stderr=True),  # Ghi vào stderr (chuẩn cho log)
        show_time=True,                # Hiện timestamp
        show_path=True,                # Hiện file + dòng code gọi log
        markup=True,                   # Cho phép [bold], [red] trong log message
        rich_tracebacks=True,          # Traceback lỗi có syntax highlighting
    )
    console_handler.setLevel(level)

    # Format: chỉ hiện message (Rich tự thêm time, level, path)
    console_format = logging.Formatter("%(message)s")
    console_handler.setFormatter(console_format)
    logger.addHandler(console_handler)

    # === Handler 2: File (tùy chọn) ===
    if log_file is not None:
        file_handler = logging.FileHandler(
            filename=log_file,
            encoding="utf-8",
            mode="a",  # append — không ghi đè file cũ
        )
        file_handler.setLevel(level)

        # Format cho file: chi tiết hơn terminal (có timestamp đầy đủ)
        file_format = logging.Formatter(
            fmt="%(asctime)s | %(levelname)-8s | %(name)s:%(funcName)s:%(lineno)d | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        file_handler.setFormatter(file_format)
        logger.addHandler(file_handler)

    # Không propagate lên root logger (tránh log bị duplicate)
    logger.propagate = False

    return logger


# Logger mặc định — import và dùng ngay
# Cách dùng: from backend.utils.logger import logger
logger = setup_logger()
