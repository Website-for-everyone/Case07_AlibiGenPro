# АРХИТЕКТУРА И СПЕЦИФИКАЦИЯ ПРОЕКТА: AlibiGen Pro

> **Проект:** AlibiGen Pro (Case 07) — Сервис генератора отмазок от дедлайнов (Y2K Vintage OS & Fake Evidence Studio)  
> **Клиент / Заказчик:** B2B Freelance & Developer Utility / Портфолио Даниэля Идрисова (@Idrisov_prod)  
> **Чек проекта:** 135 000 ₽ | **Срок:** 6 дней (Дедлайн: 2026-11-20)  
> **Дедлайн MVP (80%):** 2026-11-16  
> **Тип договора:** Договор СМЗ с ИП/ООО (Чек «Мой Налог»)

---

## 🛠 Технологический стек
- **Frontend / UI:** Vanilla JS, HTML5 Canvas 2D, CSS3 Y2K Bevel & Draggable Window System, CRT Scanline Shaders, Windows 98 / Mac OS 9 design tokens (#C0C0C0, #000080, #008080)
- **Backend & Logic:** Python 3.12, FastAPI, Uvicorn, Pillow (PIL.ImageDraw dynamic BSoD/Panic screenshot synthesis), Pydantic
- **Telegram Bot:** Aiogram 3.x, Inline Query Engine (`@AlibiGenBot`), BufferedInputFile image streaming
- **Автоматизация & Интеграции:** Telegram Inline Provider, Screenshot Evidence Exporter, Owner Telemetry to @Idrisov_prod
- **Тестирование:** Pytest, Unit & Smoke Tests

---

## 🏛 Архитектурная схема
```
[ Пользователь / Чат ] ──► [ Telegram Inline Mode (@AlibiGenBot) ]
         │                               │
         ▼                               ▼
[ Web App (Y2K Desktop) ] ──► [ Procedural Excuse Matrix ] ──► [ Canvas Evidence Renderer (BSoD/500) ]
         │                               │
         └────────► [ FastAPI Server ] ◄─┘
                          │
                          ▼
              [ Pillow Crash Image Engine ]
```

---

## 🔐 Переменные окружения (.env.example)
```env
BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrsTUVwxyz
WEB_HOST=0.0.0.0
WEB_PORT=8007
OWNER_TG_ID=1387913438
ENVIRONMENT=production
```

---

## 🔗 Ресурсы и ссылки
- **Репозиторий GitHub:** https://github.com/Website-for-everyone/Case07_AlibiGenPro
- **Dev-сервер / Preview URL:** http://localhost:8007
- **Чат проекта в Telegram:** @Idrisov_prod
