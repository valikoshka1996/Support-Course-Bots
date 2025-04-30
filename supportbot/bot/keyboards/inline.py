from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from bot.locales.strings import STRINGS

def language_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🇺🇦 Українська", callback_data="lang_uk")],
        [InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang_ru")],
        [InlineKeyboardButton(text="🇬🇧 English", callback_data="lang_en")],
    ])

def support_menu(lang):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=STRINGS[lang]['payment_btn'], callback_data="issue_payment")],
        [InlineKeyboardButton(text=STRINGS[lang]['course_btn'], callback_data="issue_course")],
        [InlineKeyboardButton(text=STRINGS[lang]['manager_btn'], callback_data="issue_manager")],
    ])
