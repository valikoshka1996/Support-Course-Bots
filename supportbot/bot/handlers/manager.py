from aiogram import Router, F
from aiogram.types import Message
from bot.bot import bot
import os
from bot.locales.strings import STRINGS
from dotenv import load_dotenv
from bot.services.db import log_request
from bot.handlers.menu import user_languages
import logging
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

router = Router()
load_dotenv()
GROUP_ID = int(os.getenv("MANAGER_GROUP_ID"))

# Зберігаємо chat_id користувача в тимчасовій змінній або БД
user_chat_ids = {}

# Логування налаштовуємо
logging.basicConfig(level=logging.DEBUG)

@router.message(F.text)
async def handle_messages(message: Message):
    # Логування кожного отриманого повідомлення
    logging.debug(f"Received message: {message.text} in chat {message.chat.id} by user {message.from_user.id}")

    # Перевірка, чи це повідомлення від користувача для менеджера
    if message.chat.id >= 0:  # Це приватний чат
        lang = user_languages.get(message.from_user.id, 'en')
        
        # Створюємо унікальну мітку для кожного користувача в каналі
        branch_title = f"User_{message.from_user.id}"

        # Формуємо текст повідомлення
        text = f"\U0001F4E9 <b>New message from the user</b>\n" \
               f"Name: {message.from_user.full_name}\n" \
               f"Username: @{message.from_user.username}\n" \
               f"User ID: {message.from_user.id}\n\n" \
               f"Message: {message.text}\n\n" \
               f"<b>Reply with:</b> /reply {message.from_user.id} your_message"

        # Записуємо chat_id користувача в словник user_chat_ids
        # Надсилаємо повідомлення в групу менеджерів з ідентифікацією користувача
# Якщо вже є ланцюг, то відповідаємо на останнє повідомлення менеджера
        reply_id = user_chat_ids.get(message.from_user.id, {}).get("last_manager_message_id")

        sent_message = await bot.send_message(
            GROUP_ID,
            f"Branch: {branch_title}\n" + text,
            reply_to_message_id=reply_id
        )

        user_chat_ids[message.from_user.id] = {
            "chat_id": message.chat.id,
            "group_message_id": sent_message.message_id,
            "last_manager_message_id": reply_id  # зберігаємо, навіть якщо None
        }


        
        await message.answer(STRINGS[lang]['waiting'])
        await log_request(user_id=message.from_user.id, message=message.text)

    elif message.text.startswith("/reply"):  # Перевірка на команду /reply

        # Ігноруємо команду, якщо вона прийшла з приватного чату
        if message.chat.type == "private":
            logging.debug("Ignoring /reply in private chat")
            return
        # Логування для відстеження, чи спрацьовує команда
        logging.debug(f"Received /reply command in chat {message.chat.id} from manager {message.from_user.id}")
        
        # Розділяємо аргументи команди
        args = message.text.split(maxsplit=1)
        if len(args) < 2:
            # Якщо формат команди неправильний
            logging.warning("Incorrect command format, missing user_id or reply_text")
            return await message.reply("Format: /reply USER_ID Your message")
        
        user_id, reply_text = args[1].split(maxsplit=1)
        
        try:
            user_id = int(user_id)  # Перетворюємо на ціле число для ID користувача
            logging.debug(f"Replying to user {user_id} with message: {reply_text}")

            # Перевіряємо, чи є chat_id цього користувача в нашому словнику
            if user_id in user_chat_ids:
    #       Надсилаємо відповідь користувачу
                await bot.send_message(user_chat_ids[user_id]["chat_id"], f"\U0001F4AC Message from the support team:\n{reply_text}")
    
            # Відповідаємо в тій самій гілці повідомлення користувача
                sent = await bot.send_message(
                    GROUP_ID,
                    f"✅ Sent to user {user_id}: {reply_text}",
                    reply_to_message_id=user_chat_ids[user_id]["group_message_id"]
                )

                # Зберігаємо ID повідомлення менеджера, щоб знати, на що відповідати
                user_chat_ids[user_id]["last_manager_message_id"] = sent.message_id


            else:
                # Якщо користувач не знайдений в словнику
                logging.warning(f"User {user_id} not found in user_chat_ids")
                await message.reply(f"❌ User {user_id} not found.")
        except Exception as e:
            # Логування помилок
            logging.error(f"Error occurred: {e}")
            await message.reply(f"❌ Error: {e}")




