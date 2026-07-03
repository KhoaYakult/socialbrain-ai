# 🧠 SocialBrain AI

**AI-powered Social Media Manager** — Nền tảng quản lý Social Media bằng AI giúp tạo nội dung, lên lịch đăng bài, và phân tích engagement tự động.

## ✨ Tính năng chính

- 🎨 **Content Generator** — Tạo caption, hashtag, script video bằng AI cho Facebook, Instagram, Threads, TikTok
- 📅 **Content Calendar** — Lên lịch đăng bài đa nền tảng
- 📊 **Analytics** — Phân tích engagement và gợi ý cải thiện
- 💬 **Auto Reply** — Trả lời comment/DM tự động bằng AI
- 🤖 **Strategy Agent** — AI Agent lên chiến lược content dài hạn
- 🔒 **Brand Knowledge** — RAG pipeline giúp AI hiểu brand của bạn

## 🛠️ Tech Stack

| Layer | Công nghệ |
|-------|-----------|
| Backend | Python 3.13 · FastAPI · Pydantic |
| AI/LLM | Google Gemini · OpenAI · Ollama |
| Vector DB | ChromaDB |
| Database | SQLite · SQLAlchemy |
| Frontend | HTML · CSS · JavaScript |

## 🚀 Cài đặt

```bash
# 1. Clone repo
git clone git@github.com:KhoaYakult/socialbrain-ai.git
cd socialbrain-ai

# 2. Tạo virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux

# 3. Cài dependencies
pip install -r requirements.txt

# 4. Cấu hình API key
copy .env.example .env
# Mở .env và điền API key của bạn

# 5. Chạy server
uvicorn backend.main:app --reload
```

## 📁 Cấu trúc dự án

```
socialbrain-ai/
├── backend/                # Python FastAPI backend
│   ├── main.py             # Entry point
│   ├── config.py           # Cấu hình & biến môi trường
│   ├── routers/            # API endpoints
│   ├── services/           # Business logic
│   ├── models/             # Pydantic schemas
│   └── utils/              # Helpers & logging
├── frontend/               # Web dashboard (HTML/CSS/JS)
├── data/                   # Sample data
├── tests/                  # Unit & integration tests
└── docs/                   # Documentation
```

## 📝 Roadmap

Dự án được xây dựng theo [AI Engineer Roadmap](https://roadmap.sh/ai-engineer):

- [x] Phase 0: Project Setup & Git
- [ ] Phase 1: LLM Gateway (Multi-provider)
- [ ] Phase 2: Content Generator (Prompt Engineering)
- [ ] Phase 3: Brand Knowledge Base (RAG)
- [ ] Phase 4: Content Calendar
- [ ] Phase 5: AI Agent
- [ ] Phase 6: Open Source AI (Ollama)
- [ ] Phase 7: Comment Auto-Reply
- [ ] Phase 8: Analytics & Safety
- [ ] Phase 9: Polish & Launch

## 📄 License

MIT License — Xem [LICENSE](LICENSE) để biết thêm chi tiết.

## 👤 Author

**KhoaYakult** — [GitHub](https://github.com/KhoaYakult)
