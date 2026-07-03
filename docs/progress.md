# 📊 SocialBrain AI — Quản lý tiến độ dự án

> Cập nhật lần cuối: 2026-07-03

---

## Tổng quan Phase

| Phase | Tên | Trạng thái | Ngày bắt đầu | Ngày hoàn thành |
|-------|-----|------------|---------------|-----------------|
| 0 | Cài đặt môi trường & Git | 🔄 Đang làm | 2026-06-22 | — |
| 1 | LLM Gateway | ⬜ Chưa bắt đầu | — | — |
| 2 | Content Generator | ⬜ Chưa bắt đầu | — | — |
| 3 | Brand Knowledge Base (RAG) | ⬜ Chưa bắt đầu | — | — |
| 4 | Content Calendar | ⬜ Chưa bắt đầu | — | — |
| 5 | AI Agent | ⬜ Chưa bắt đầu | — | — |
| 6 | Open Source AI (Ollama) | ⬜ Chưa bắt đầu | — | — |
| 7 | Comment Auto-Reply | ⬜ Chưa bắt đầu | — | — |
| 8 | Analytics & Safety | ⬜ Chưa bắt đầu | — | — |
| 9 | Polish & Launch | ⬜ Chưa bắt đầu | — | — |

---

## Phase 0: Cài đặt môi trường & Git

### Lý thuyết đã học
- [x] Git là gì? Version Control, 3 vùng (Working Dir → Staging → Local Repo → Remote)
- [x] Commit = snapshot toàn bộ project tại 1 thời điểm
- [x] Git vs GitHub (engine local vs dịch vụ cloud)
- [x] SSH Key — mã hóa bất đối xứng (public/private key)
- [x] Separation of Concerns — kiến trúc phân lớp (Router → Service → Model → Utils)
- [x] Python Module vs Package, vai trò của `__init__.py`
- [ ] `.gitignore` và bảo mật API keys
- [ ] Virtual environment (venv) là gì

### Thực hành đã làm
- [x] Bước 0.1: Lý thuyết Git
- [x] Bước 0.2: Cấu hình Git (`user.name`, `user.email`)
- [x] Bước 0.3: Tạo SSH Key Ed25519 + thêm vào GitHub
- [x] Bước 0.4: `git init` + `git remote add origin`
- [x] Bước 0.5: Lý thuyết cấu trúc dự án Python
- [x] Bước 0.6: Tạo file khung (README, config, main, logger...)
- [ ] Bước 0.7: Lý thuyết `.gitignore` & bảo mật
- [ ] Bước 0.8: First commit + push lên GitHub
- [ ] Bước 0.9: Lý thuyết Virtual Environment
- [ ] Bước 0.10: Tạo venv + cài FastAPI + chạy server

### Kiến thức Git đã dùng
| Lệnh | Ý nghĩa | Bước |
|-------|---------|------|
| `git config --global` | Cấu hình tên/email | 0.2 |
| `ssh-keygen -t ed25519` | Tạo SSH key | 0.3 |
| `ssh -T git@github.com` | Test kết nối SSH | 0.3 |
| `git init` | Khởi tạo repo local | 0.4 |
| `git remote add origin` | Liên kết với GitHub | 0.4 |
| `git status` | Xem trạng thái hiện tại | 0.6 |

### Files đã tạo
| File | Chức năng |
|------|-----------|
| `README.md` | Bộ mặt dự án trên GitHub |
| `requirements.txt` | Danh sách thư viện Python |
| `.env.example` | Template biến môi trường |
| `.env` | Biến môi trường thật (gitignored) |
| `.gitignore` | Danh sách file Git bỏ qua |
| `backend/__init__.py` | Package marker |
| `backend/config.py` | Trung tâm cấu hình (pydantic-settings) |
| `backend/main.py` | Entry point FastAPI |
| `backend/utils/logger.py` | Hệ thống logging (Rich) |

---

## Ghi chú & Quyết định kỹ thuật

| Quyết định | Lý do |
|------------|-------|
| Dùng SSH thay vì HTTPS | Không cần nhập token mỗi lần push |
| Dùng Ed25519 thay vì RSA | Nhanh hơn, an toàn hơn, key ngắn hơn |
| Dùng `pydantic-settings` thay vì `os.getenv` | Type-safe, auto-convert, báo lỗi rõ |
| Dùng `@lru_cache` cho Settings | Singleton pattern, chỉ đọc .env 1 lần |
| Dùng `Rich` cho logging | Terminal đẹp, có màu, dễ debug |
| Layered Architecture | Tách biệt trách nhiệm, dễ test, dễ mở rộng |
