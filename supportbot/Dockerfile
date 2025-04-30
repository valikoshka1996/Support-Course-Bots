# Вказуємо базовий образ
FROM python:3.10-slim

# Встановлюємо робочу директорію
WORKDIR /app

# Копіюємо файл requirements.txt в контейнер
COPY requirements.txt .

# Встановлюємо залежності з requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо весь проект в контейнер
COPY . .

# Вказуємо команду для запуску бота
CMD ["python3", "-m", "bot.bot"]
