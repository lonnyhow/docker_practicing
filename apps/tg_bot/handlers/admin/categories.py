from apps.tg_bot.data.loader import bot
from telebot import types
from apps.tg_bot.utils import is_admin
from apps.tg_bot.keyboards.inline import show_table_actions_kb, get_categories, show_table_items_actions_kb
from apps.main.models import Category


def get_message_and_chat_id(call: types.CallbackQuery) -> tuple:
    return call.message.chat.id, call.message.message_id

@bot.message_handler(func=lambda message: message.text == 'Категории' and is_admin)
def handle_admin_categorise(message):
    bot.reply_to(message, 'Выберите действие над категориями', reply_markup=show_table_actions_kb('categories'))

@bot.callback_query_handler(func=lambda call: call.data == 'table_get_categories' and is_admin)
def handle_categories_get(call: types.CallbackQuery):
    chat_id, message_id = get_message_and_chat_id(call)

    categories = Category.objects.all()
    bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text='Выберите Категорию',
        reply_markup=get_categories(categories)
    )

@bot.callback_query_handler(
    func=lambda call: call.data.startswith('get_category') and is_admin
)
def handle_categories_actions(call: types.CallbackQuery):
    chat_id, message_id = get_message_and_chat_id(call)


    category_id = call.data.split(':')[-1]
    category_object = Category.objects.get(id=category_id)

    bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text=f'Choose the action below for category: <b>{category_object.name}</b>',
        reply_markup=show_table_items_actions_kb('category', category_object.id)
    )
@bot.callback_query_handler(
    func=lambda call: call.data.startswith('delete_category') and is_admin
)
def handle_category_delete(call: types.CallbackQuery):
    category_id = int(call.data.split(':')[-1])

    chat_id, message_id = get_message_and_chat_id(call)

    category = Category.objects.get(id=category_id)

    bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text=f'Do you want to delete category: <b>{category.name}</b>?',
    )

@bot.callback_query_handler(
    func=lambda call: call.data.startswith('update_category') and is_admin
)
def handle_update_category(call: types.CallbackQuery):
    chat_id, message_id = get_message_and_chat_id(call)
    bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text='Write the title for the new category',
    )