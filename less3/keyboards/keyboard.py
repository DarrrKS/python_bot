from aiogram import types

button1 = types.KeyboardButton(text='/start')
button2 = types.KeyboardButton(text='/prof')
button3 = types.KeyboardButton(text='Info')
button4 = types.KeyboardButton(text='show fox')
button5 = types.KeyboardButton(text='close')

keybord1 = [
    [button1, button2, button3],
    [button4, button5]
]

keybord2 = [
    [button4, button5]
]

kb1 = types.ReplyKeyboardMarkup(keyboard=keybord1, resize_keyboard=True)
kb2 = types.ReplyKeyboardMarkup(keyboard=keybord2, resize_keyboard=True)