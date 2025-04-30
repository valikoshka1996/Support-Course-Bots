import os
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, BotCommand
from telegram.ext import (
    ApplicationBuilder, CommandHandler, CallbackQueryHandler,
    ContextTypes
)
import nest_asyncio
import asyncio

# Завантаження змінних із .env
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
COURSE_UA = os.getenv("COURSE_UA")
COURSE_RU = os.getenv("COURSE_RU")
COURSE_EN = os.getenv("COURSE_EN")
BLOG_UA = os.getenv("BLOG_UA")
BLOG_RU = os.getenv("BLOG_RU")
BLOG_EN = os.getenv("BLOG_EN")

# Переклади
messages = {
    'ua': {
        'start': 'Оберіть мову/Выберите язык/Choose a language:',
        'course': 'Доступ до курсу: 🔗 {course}\nДоступ до закритого чату обговорення курсу: 🔗 {blog}',
    },
    'ru': {
        'start': 'Оберіть мову/Выберите язык/Choose a language:',
        'course': 'Доступ к курсу: 🔗 {course}\nДоступ к закрытому чату обсуждения курса: 🔗 {blog}',
    },
    'en': {
        'start': 'Оберіть мову/Выберите язык/Choose a language:',
        'course': 'Access to the course: 🔗 {course}\nAccess to the closed discussion chat: 🔗 {blog}',
    },
}

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Ukrainian 🇺🇦", callback_data='ua')],
        [InlineKeyboardButton("Russian 🇷🇺", callback_data='ru')],
        [InlineKeyboardButton("English 🇬🇧", callback_data='en')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(messages['ua']['start'], reply_markup=reply_markup)

# Обробка вибору мови через кнопки
async def language_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    lang_code = query.data
    course = {'ua': COURSE_UA, 'ru': COURSE_RU, 'en': COURSE_EN}[lang_code]
    blog = {'ua': BLOG_UA, 'ru': BLOG_RU, 'en': BLOG_EN}[lang_code]

    text = messages[lang_code]['course'].format(course=course, blog=blog)
    await query.edit_message_text(text=text)

# Запуск бота
async def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    # Додаємо кнопку /start в меню бота
    await app.bot.set_my_commands([BotCommand("start", "Почати / Start the bot")])

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(language_callback))

    await app.run_polling()

# Асинхронний запуск
if __name__ == '__main__':
    nest_asyncio.apply()  # Додаємо підтримку для вже існуючого event loop
    asyncio.run(main())  # Запускаємо основний процес
