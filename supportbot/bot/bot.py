import asyncio
import logging
import os
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import BotCommand
from dotenv import load_dotenv



load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

# Окрема функція для реєстрації обробників
async def setup_handlers():
    from bot.handlers.start import router as start_router
    from bot.handlers.menu import router as menu_router
    from bot.handlers.manager import router as manager_router
    dp.include_routers(start_router, menu_router, manager_router)

# Функція для налаштування меню команд
# Функція для налаштування меню команд
async def set_commands():
    from aiogram.types import BotCommandScopeDefault, BotCommandScopeAllGroupChats

    # Команда /start — лише для приватних чатів (Default)
    private_commands = [
        BotCommand(command="/start", description="Start the bot"),
    ]
    await bot.set_my_commands(private_commands, scope=BotCommandScopeDefault())
    
    group_commands = [
        BotCommand(command="/reply", description="reply to the user: /reply USER_ID Message")
    ]
    
    # Реєструємо команди для всіх групових чатів
    await bot.set_my_commands(group_commands, scope=BotCommandScopeAllGroupChats())
    
# Основна функція для запуску бота
async def main():
    logging.basicConfig(level=logging.INFO)
    
    # Налаштовуємо команди меню
    await set_commands()

    await bot.delete_webhook(drop_pending_updates=True)
    
    # Спочатку реєструємо обробники
    await setup_handlers()
    
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
