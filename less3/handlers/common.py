from aiogram import types, F, Router
from aiogram.filters.command import Command
import logging
from datetime import datetime 
from aiogram.types import Message
from aiogram import html
from keyboards.keyboard import kb1, kb2
from utils.random_fox import fox

router= Router()

#handler to command/start
@router.message(Command('start'))
async def start(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'hello, {name}', reply_markup=kb1)

#handler to show fox
@router.message(Command('fox'))
@router.message(Command('лиса'))
@router.message(F.text.lower() == 'show fox')
async def show_fox(message: types.Message):
    name = message.chat.first_name
    image_fox = fox()
    await message.answer(f'Hey hold the fox, {name}')   
    await message.answer_photo(photo=image_fox)



#def condition
@router.message(F.text)
async def condition_def(message: types.Message):
    msg_user = message.text.lower()
    name = message.chat.first_name
    if "info" in msg_user:
        time_now = datetime.now().strftime('%H:%M')
        await message.answer(f"Time now, {time_now}\n\n{name}")
    elif "stop" == msg_user:
        await message.answer(f'Bye my friend, {name}')  
    elif "who are you" in msg_user:
        await message.answer(f'Im bot, {name}')  
    elif "fox" in msg_user:
        await message.answer(f'Hey Look at this what i have, {name}', reply_markup=kb2)
    else: 
        await message.answer(f'Sorry, I dont know such a word')

#time checker
@router.message(F.text)
async def def_chek(message: Message):
    #get time 
    time_now =datetime.now().strftime('%H:%M')
    #create underline text
    add_text = html.underline(f"Created in {time_now}")
    #send to new message with added text
    await message.answer(f"{message.html_text}\n\n{add_text}", parse_mode="HTML")

