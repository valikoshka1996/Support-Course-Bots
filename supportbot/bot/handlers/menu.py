from aiogram import Router, F
from aiogram.types import CallbackQuery
from bot.keyboards.inline import support_menu
from bot.locales.strings import STRINGS
from aiogram.fsm.context import FSMContext

router = Router()

user_languages = {}

@router.callback_query(F.data.startswith("lang_"))
async def set_language(callback: CallbackQuery):
    lang = callback.data.split("_")[1]
    user_languages[callback.from_user.id] = lang
    await callback.message.answer(STRINGS[lang]['menu'], reply_markup=support_menu(lang))
    await callback.answer()

@router.callback_query(F.data.startswith("issue_"))
async def issue_selected(callback: CallbackQuery):
    lang = user_languages.get(callback.from_user.id, 'en')
    issue = callback.data.split("_")[1]
    await callback.message.answer(STRINGS[lang][issue])
    if issue != "manager":
        await callback.message.answer(STRINGS[lang]['menu'], reply_markup=support_menu(lang))
    await callback.answer()
