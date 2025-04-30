Based on the extracted contents and main scripts, here are two detailed `README.md` files for each project.

---

## 📦 `supportbot` - README.md


# SupportBot

SupportBot is a Telegram bot built using the `aiogram` framework that serves as a support assistant, enabling interaction between users and a manager via structured menus and commands. It includes support for asynchronous handling, environment configuration, and Docker deployment.

---

## 📌 Features

- Language selection and multilingual command descriptions
- `/start` and main menu handler
- User-to-manager message routing system
- SQLite logging for requests
- Dockerized for easy deployment

---

## 🧰 Technologies Used

- Python 3.10
- [aiogram](https://docs.aiogram.dev) (async Telegram Bot Framework)
- SQLite
- Docker + Docker Compose
- Python-dotenv for environment configuration

---

## 📂 Project Structure

```
supportbot/
├── bot/
│   ├── bot.py               # Main entrypoint
│   └── handlers/            # Routers: start, menu, manager
├── database.db              # SQLite DB for logging
├── .env                     # Environment variables (not committed)
├── requirements.txt         # Python dependencies
├── Dockerfile               # Docker image for bot
└── docker-compose.yml       # Compose for easy deployment
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone <repo-url>
cd supportbot
```

### 2. Setup Environment

Create a `.env` file:

```env
BOT_TOKEN=your_telegram_bot_token
```

### 3. Install Dependencies (Optional for local use)

```bash
pip install -r requirements.txt
```

### 4. Run the Bot (Locally)

```bash
python3 -m bot.bot
```

### 5. Run via Docker

```bash
docker-compose up --build -d
```

---

## 📋 Commands

| Command | Description          |
|---------|----------------------|
| /start  | Start interaction    |

---

## 🛠 Handlers

- `start.py` – initializes the bot
- `menu.py` – shows available options
- `manager.py` – handles messaging with a manager

---

## 🗃 Database

All incoming requests are logged in `database.db`.

---

## 🧑‍💼 Manager Functionality

Messages from users are routed to a manager for personal support. The manager can respond via Telegram.

---

## 📄 License

MIT License
```

---

## 🎓 `coursebot` - README.md

# CourseBot

CourseBot is a simple Telegram bot that provides users with course access links and blog discussions in multiple languages. Built using the official `python-telegram-bot` library, it supports inline button interaction and internationalization.

---

## 📌 Features

- Language selection at start
- Returns course + blog access links
- Environment-based configuration
- Dockerized deployment
- Simple UX with inline buttons

---

## 🧰 Technologies Used

- Python 3.12
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- `dotenv` for config
- `nest_asyncio` to allow nested loops in async
- Docker + Docker Compose

---

## 📂 Project Structure

```
coursebot/
├── bot.py                 # Main bot script
├── .env                   # Environment variables
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker build configuration
├── docker-compose.yml     # For container orchestration
└── tg/                    # Virtual environment (optional in repo)
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone <repo-url>
cd coursebot
```

### 2. Create .env File

```env
TELEGRAM_TOKEN=your_telegram_bot_token
COURSE_UA=https://course.ua.link
COURSE_RU=https://course.ru.link
COURSE_EN=https://course.en.link
BLOG_UA=https://blog.ua.link
BLOG_RU=https://blog.ru.link
BLOG_EN=https://blog.en.link
```

### 3. Install Dependencies (For Local Use)

```bash
pip install -r requirements.txt
```

### 4. Run the Bot

```bash
python3 bot.py
```

---

## 🐳 Docker Deployment

```bash
docker-compose up --build -d
```

---

## 💬 Languages Supported

- Ukrainian 🇺🇦
- Russian 🇷🇺
- English 🇬🇧

---

## 🤖 Bot Flow

1. `/start` prompts user to choose language.
2. Inline buttons are used for language selection.
3. Bot sends course and blog links in selected language.

---

## 📄 License

MIT License
```

Would you like me to save these as `README.md` files in their respective folders?
