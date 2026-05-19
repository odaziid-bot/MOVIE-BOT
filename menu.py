import asyncio
from aiogram import Bot, Dispatcher, F, types, Router
from aiogram.types import FSInputFile, Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage

from user_base import user_db
from keyboards import fav_genre_key
from user_state import User
from keyboards import menu_key
from movies import western, comedy, horror, action, sci_fi
from keyboards import chek_1, chek_2, chek_3, chek_4, chek_5
from keyboards import choice_key
from keyboards import menu_do
from keyboards import linkme1, linkme2, linkme3, linkme4, linkme5, linkme6, linkme7, linkme8, linkme9, linkme10, linkme11, linkme12, linkme13, linkme14, linkme15

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привет! Я твой путеводитель в мире фильмов 🦸‍♂️\nГотов ли ты его исследовать?", reply_markup=menu_key)

@router.callback_query(F.data == "get_yes_menu")
async def get_yes_menu_handler(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.set_state(User.name)
    await callback.message.answer("Хорошо!")
    await asyncio.sleep(2)
    await callback.message.answer("Но перед тем как мы начнем, пожалуйста, укажи свое имя")

@router.message(F.text, User.name)
async def user_name_process(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    data = await state.get_data()
    mes1 = await message.answer(f"Хорошо, {data['name']}.")
    await asyncio.sleep(2)
    await message.answer("Теперь, мне важно узнать твой любимый жанр", reply_markup=fav_genre_key())
    await state.set_state(User.fav_genre)

@router.message(F.text, User.fav_genre)
async def user_fav_genre_process(message: Message, state: FSMContext):
    await state.update_data(fav_genre=message.text)
    data = await state.get_data()
    await message.answer(f"{data['fav_genre']} — отличный выбор!")
    name = data.get('name')
    fav_genre = data.get('fav_genre')
    user_db(name, fav_genre)
    await asyncio.sleep(2)
    await message.answer("Готов увидеть свою подборку?", reply_markup=choice_key)
    await state.set_state(None)

@router.callback_query(F.data == "get_no_ch")
async def choice_n0_handler(callback: CallbackQuery):
    await callback.answer()
    mes2 = await callback.message.answer("Окей!")
    await asyncio.sleep(2)
    await mes2.edit_text("Как передумаешь, приходи заново 😉")

@router.callback_query(F.data == "get_yes_ch")
async def choice_handler(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    data = await state.get_data()
    if data['fav_genre'] == "ВЕСТЕРН 🤠🏜️":
        await callback.message.answer("ГОТОВО", reply_markup=chek_1)
    elif data['fav_genre'] == "КОМЕДИЯ 🤣":
        await callback.message.answer("ГОТОВО", reply_markup=chek_2)
    elif data['fav_genre'] == "УЖАСЫ 👻":
        await callback.message.answer("ГОТОВО", reply_markup=chek_3)
    elif data['fav_genre'] == "БОЕВИК 🔫":
        await callback.message.answer("ГОТОВО", reply_markup=chek_4)
    elif data['fav_genre'] == "НАУЧНАЯ ФАНТАСТИКА 🚀":
        await callback.message.answer("ГОТОВО", reply_markup=chek_5)
    
    

@router.callback_query(F.data == "get_chek_1")
async def mov1_list(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("ПОДБОРКА:", reply_markup=menu_do())
    await callback.message.answer(f"НАЗВАНИЕ:\n{western[0]['name']}\n\nОПИСАНИЕ:\n{western[0]['descript']}", reply_markup=linkme1)
    await asyncio.sleep(1)
    await callback.message.answer(f"НАЗВАНИЕ:\n{western[1]['name']}\n\nОПИСАНИЕ:\n{western[1]['descript']}", reply_markup=linkme2)
    await asyncio.sleep(1)
    await callback.message.answer(f"НАЗВАНИЕ:\n{western[2]['name']}\n\nОПИСАНИЕ:\n{western[2]['descript']}", reply_markup=linkme3)

@router.callback_query(F.data == "get_chek_2")
async def mov2_list(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("ПОДБОРКА:", reply_markup=menu_do())
    await callback.message.answer(f"НАЗВАНИЕ:\n{comedy[0]['name']}\n\nОПИСАНИЕ:\n{comedy[0]['descript']}", reply_markup=linkme4)
    await asyncio.sleep(1)
    await callback.message.answer(f"НАЗВАНИЕ:\n{comedy[1]['name']}\n\nОПИСАНИЕ:\n{comedy[1]['descript']}", reply_markup=linkme5)
    await asyncio.sleep(1)
    await callback.message.answer(f"НАЗВАНИЕ:\n{comedy[2]['name']}\n\nОПИСАНИЕ:\n{comedy[2]['descript']}", reply_markup=linkme6)

@router.callback_query(F.data == "get_chek_3")
async def mov3_list(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("ПОДБОРКА:", reply_markup=menu_do())
    await callback.message.answer(f"НАЗВАНИЕ:\n{horror[0]['name']}\n\nОПИСАНИЕ:\n{horror[0]['descript']}",  reply_markup=linkme7)
    await asyncio.sleep(1)
    await callback.message.answer(f"НАЗВАНИЕ:\n{horror[1]['name']}\n\nОПИСАНИЕ:\n{horror[1]['descript']}",  reply_markup=linkme8)
    await asyncio.sleep(1)
    await callback.message.answer(f"НАЗВАНИЕ:\n{horror[2]['name']}\n\nОПИСАНИЕ:\n{horror[2]['descript']}",  reply_markup=linkme9)

@router.callback_query(F.data == "get_chek_4")
async def mov4_list(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("ПОДБОРКА:", reply_markup=menu_do())
    await callback.message.answer(f"НАЗВАНИЕ:\n{action[0]['name']}\n\nОПИСАНИЕ:\n{action[0]['descript']}", reply_markup=linkme10)
    await asyncio.sleep(1)
    await callback.message.answer(f"НАЗВАНИЕ:\n{action[1]['name']}\n\nОПИСАНИЕ:\n{action[1]['descript']}",  reply_markup=linkme11)
    await asyncio.sleep(1)
    await callback.message.answer(f"НАЗВАНИЕ:\n{action[2]['name']}\n\nОПИСАНИЕ:\n{action[2]['descript']}",  reply_markup=linkme12)

@router.callback_query(F.data == "get_chek_5")
async def mov5_list(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("ПОДБОРКА:", reply_markup=menu_do())
    await callback.message.answer(f"НАЗВАНИЕ:\n{sci_fi[0]['name']}\n\nОПИСАНИЕ:\n{sci_fi[0]['descript']}", reply_markup=linkme13)
    await asyncio.sleep(1)
    await callback.message.answer(f"НАЗВАНИЕ:\n{sci_fi[1]['name']}\n\nОПИСАНИЕ:\n{sci_fi[1]['descript']}", reply_markup=linkme14)
    await asyncio.sleep(1)
    await callback.message.answer(f"НАЗВАНИЕ:\n{sci_fi[2]['name']}\n\nОПИСАНИЕ:\n{sci_fi[2]['descript']}", reply_markup=linkme15)

@router.callback_query(F.data == "get_chek_2")
async def mov2_list(callback: CallbackQuery):
    await callback.answer()

@router.callback_query(F.data == "get_no_menu")
async def get_no_menu_handler(callback: CallbackQuery):
    await callback.answer()
    mes2 = await callback.message.answer("Хорошо")
    await asyncio.sleep(2)
    await mes2.edit_text("Когда передумаете введите /start 😉")

