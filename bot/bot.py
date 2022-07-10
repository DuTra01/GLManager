import telebot

from .bot_config import BOT_TOKEN

if BOT_TOKEN is None:
    raise Exception('Bot token is not set')

bot = telebot.TeleBot(
    BOT_TOKEN,
    skip_pending=True,
    parse_mode='HTML',
)