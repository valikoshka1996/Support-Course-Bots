from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from bot.keyboards.inline import language_keyboard

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    if message.chat.type != "private":
        return  # ігноруємо, якщо не приватний чат

    await message.answer(
        "\U0001F44B Choose the language / Оберіть мову / Выберите язык:",
        reply_markup=language_keyboard()
    )
