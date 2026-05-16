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

from movies import western, comedy, horror, action, sci_fi
from keyboards import fav_genre_key_1
from keyboards import menu_do

router = Router()

@router.message(F.text == "Вернуться ♻️")
async def return_menu(message: Message):
    await message.answer("ВАШЕ МЕНЮ:", reply_markup=fav_genre_key_1())

@router.message(F.text == "Вестерн 🤠🏜️")
async def ret_menu_handler_1(message: Message):
    await message.answer("ПОДБОРКА:", reply_markup=menu_do())
    await message.answer(f"НАЗВАНИЕ:\n{western[0]['name']}\n\nОПИСАНИЕ:\n{western[0]['descript']}")
    await asyncio.sleep(1)
    await message.answer(f"НАЗВАНИЕ:\n{western[1]['name']}\n\nОПИСАНИЕ:\n{western[1]['descript']}")
    await asyncio.sleep(1)
    await message.answer(f"НАЗВАНИЕ:\n{western[2]['name']}\n\nОПИСАНИЕ:\n{western[2]['descript']}")

@router.message(F.text == "Комедия 🤣")
async def ret_menu_handler_2(message: Message):
    await message.answer("ПОДБОРКА:", reply_markup=menu_do())
    await message.answer(f"НАЗВАНИЕ:\n{comedy[0]['name']}\n\nОПИСАНИЕ:\n{comedy[0]['descript']}")
    await asyncio.sleep(1)
    await message.answer(f"НАЗВАНИЕ:\n{comedy[1]['name']}\n\nОПИСАНИЕ:\n{comedy[1]['descript']}")
    await asyncio.sleep(1)
    await message.answer(f"НАЗВАНИЕ:\n{comedy[2]['name']}\n\nОПИСАНИЕ:\n{comedy[2]['descript']}")

@router.message(F.text == "Ужасы 👻")
async def ret_menu_handler_3(message: Message):
    await message.answer("ПОДБОРКА:", reply_markup=menu_do())
    await message.answer(f"НАЗВАНИЕ:\n{horror[0]['name']}\n\nОПИСАНИЕ:\n{horror[0]['descript']}")
    await asyncio.sleep(1)
    await message.answer(f"НАЗВАНИЕ:\n{horror[1]['name']}\n\nОПИСАНИЕ:\n{horror[1]['descript']}")
    await asyncio.sleep(1)
    await message.answer(f"НАЗВАНИЕ:\n{horror[2]['name']}\n\nОПИСАНИЕ:\n{horror[2]['descript']}")

@router.message(F.text == "Боевик 🔫")
async def ret_menu_handler_4(message: Message):
    await message.answer("ПОДБОРКА:", reply_markup=menu_do())
    await message.answer(f"НАЗВАНИЕ:\n{action[0]['name']}\n\nОПИСАНИЕ:\n{action[0]['descript']}")
    await asyncio.sleep(1)
    await message.answer(f"НАЗВАНИЕ:\n{action[1]['name']}\n\nОПИСАНИЕ:\n{action[1]['descript']}")
    await asyncio.sleep(1)
    await message.answer(f"НАЗВАНИЕ:\n{action[2]['name']}\n\nОПИСАНИЕ:\n{action[2]['descript']}")

@router.message(F.text == "Научная фантастика🚀")
async def ret_menu_handler_5(message: Message):
    await message.answer("ПОДБОРКА:", reply_markup=menu_do())
    await message.answer(f"НАЗВАНИЕ:\n{sci_fi[0]['name']}\n\nОПИСАНИЕ:\n{sci_fi[0]['descript']}")
    await asyncio.sleep(1)
    await message.answer(f"НАЗВАНИЕ:\n{sci_fi[1]['name']}\n\nОПИСАНИЕ:\n{sci_fi[1]['descript']}")
    await asyncio.sleep(1)
    await message.answer(f"НАЗВАНИЕ:\n{sci_fi[2]['name']}\n\nОПИСАНИЕ:\n{sci_fi[2]['descript']}")
