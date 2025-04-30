# Вибір базового образу
FROM python:3.9-slim

# Встановлення залежностей
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

# Запуск бота
CMD ["python", "bot.py"]
