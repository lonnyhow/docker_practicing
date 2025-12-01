from apps.tg_bot.data.loader import bot
from apps.tg_bot.keyboards.reply import default_kb

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        chat_id=message.chat.id,
        text='Hello',
        reply_markup=default_kb()
    )

@bot.message_handler(func=lambda message: message.text == 'Вопросы и ответы')
def handle_message(message):
    bot.reply_to(message, message.text)

