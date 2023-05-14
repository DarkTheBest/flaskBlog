from telebot import TeleBot
from .config import token, admin_id
from authentication.models import User


bot = TeleBot(token=token)


def send_message(username, email, message):
    return bot.send_message(
        chat_id=admin_id,
        text=f"Сообщение от пользователя:\nusername: {username}\nemail: {email}\nсообщение: {message}"
    )

