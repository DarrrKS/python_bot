from aiogram import types, F, Router
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards.prof_keyboards import make_row_keyboard

router= Router()

availoble_prof_names = ["Developer", "Analitic", "Tester"]
availoble_prof_grades = ["Junior", "Middle", "Senior"]

class ChooseProfNames(StatesGroup):
    choose_prof_name = State()
    choose_prof_grades = State()



#handler to command/prof
@router.message(Command('prof'))
async def cmd_prof(message: types.Message, state: FSMContext):
    name = message.chat.first_name
    await message.answer(f'Hello, {name}, choose your profession',
                          reply_markup=make_row_keyboard(availoble_prof_names))
    await state.set_state(ChooseProfNames.choose_prof_name)


#state for prof_names
@router.message(ChooseProfNames.choose_prof_name, F.text.in_(availoble_prof_names))
async def prof_name(message: types.Message, state: FSMContext):
    await state.update_data(chosen_prof=message.text.lower())
    await message.answer(f'Thank you, Now choose your level',
                          reply_markup=make_row_keyboard(availoble_prof_grades))
    await state.set_state(ChooseProfNames.choose_prof_grades)


#rechoose_prof
@router.message(ChooseProfNames.choose_prof_name)
async def prof_incorrectly(message: types.Message):
    await message.answer(f'I do not know such a profession, Rechoose your profession pls!',
                          reply_markup=make_row_keyboard(availoble_prof_names))
    
#final results
@router.message(ChooseProfNames.choose_prof_grades, F.text.in_(availoble_prof_grades))
async def grade_chosen(message: types.Message, state: FSMContext):
    user_date = await state.get_data()
    await message.answer(f'You Chosen the {message.text.lower()} level. Your profession is {user_date.get("chosen_prof")}',
                          reply_markup=types.ReplyKeyboardRemove())
    await state.clear()


#handler to command/rechoose_grades
@router.message(ChooseProfNames.choose_prof_grades)
async def cmd_grades_incorrectly(message: types.Message):
    await message.answer(f'I do not know such a level, Rechoose your level pls!',
                          reply_markup=make_row_keyboard(availoble_prof_grades))
