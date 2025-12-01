from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def show_admin_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    kb.add(
      KeyboardButton('Пользователи'),
            KeyboardButton('Категории'),
            KeyboardButton('Коментарии'),
            KeyboardButton('Посты'))
    return kb
def default_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    kb.add(
      KeyboardButton('Вопросы и ответы'),
    )
    return kb

