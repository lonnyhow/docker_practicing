from apps.tg_bot.data.loader import bot
from telebot import types
from apps.tg_bot.keyboards.reply import show_admin_kb
from apps.tg_bot.utils import is_admin


@bot.message_handler(commands=['start'], func=is_admin)
def handle_admin_start(message: types.Message):
    bot.reply_to(message, 'Вы админ', reply_markup=show_admin_kb())

@bot.message_handler(func=lambda message: message.text == 'Пользователи' and is_admin)
def handle_admin_users(message):
    bot.reply_to(message, 'Все пользователи')


@bot.message_handler(func=lambda message: message.text == 'Коментарии' and is_admin)
def handle_admin_comments(message):
    bot.reply_to(message, "Все коментарии")

@bot.message_handler(func=lambda message: message.text == 'Посты' and is_admin)
def handle_admin_posts(message):
    bot.reply_to(message, "Все посты")

