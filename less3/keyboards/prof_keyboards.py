from aiogram import types

def make_row_keyboard(itoms:list[str])-> types.ReplyKeyboardMarkup:
    row = [types.KeyboardButton(text=itom) for itom in itoms]
    return types.ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True)


