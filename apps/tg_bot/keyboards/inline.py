from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# from apps.blog_api.routes.v1 import categories

def show_table_actions_kb(table_name):
    kb = InlineKeyboardMarkup()
    kb.add(
        InlineKeyboardButton(text='Добавить', callback_data=f'table_add_{table_name}'),
        InlineKeyboardButton(text='Получить', callback_data=f'table_get_{table_name}'),
    )
    return kb

def get_categories(categories):
    kb = InlineKeyboardMarkup(row_width=2)
    buttons = []
    for category in categories:
        buttons.append(
            InlineKeyboardButton(text=category.name, callback_data=f'get_category:{category.id}')
        )
    kb.add(*buttons)
    return kb
def show_table_items_actions_kb(item_name: str, item_id:int):
    kb = InlineKeyboardMarkup()
    kb.add(
        InlineKeyboardButton(text='Delete', callback_data=f'delete_{item_name}:{item_id}'),
        InlineKeyboardButton(text='Update', callback_data=f'update_{item_name}:{item_id}'),
    )
    return kb
