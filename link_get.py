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

router = Router()

@router.callback_query(F.data == "link1_1")
async def lin1_1_handler(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("ССЫЛКА НА ФИЛЬМ:\nhttps://kinogo.media/18231-odnazhdy-na-dikom-zapade.html\nПриятного просмотра ✨✨✨")

@router.callback_query(F.data == "link1_2")
async def lin1_2_handler(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("ССЫЛКА НА ФИЛЬМ:\nhttps://kinogo.online/filmy/26027-horoshij-plohoj-zloj.html\nПриятного просмотра ✨✨✨")

@router.callback_query(F.data == "link1_3")
async def lin1_3_handler(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("ССЫЛКА НА ФИЛЬМ:\nhttps://kinogo.online/filmy/3679-neproschennyj.html\nПриятного просмотра ✨✨✨")

@router.callback_query(F.data == "link2_1")
async def lin2_1(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("ССЫЛКА НА ФИЛЬМ:\nhttps://kinogo.online/filmy/17778-golyj-pistolet.html\nПриятного просмотра ✨✨✨")
    
@router.callback_query(F.data == "link2_2")
async def lin2_2(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("ССЫЛКА НА ФИЛЬМ:\nhttps://kinogo.media/30356-v-dzhaze-tolko-devushki.html\nПриятного просмотра ✨✨✨")
    
@router.callback_query(F.data == "link2_3")
async def lin2_3(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("ССЫЛКА НА ФИЛЬМ:\nhttps://kinogo.online/filmy/17082-jenni-holl.html\nПриятного просмотра ✨✨✨")
    
@router.callback_query(F.data == "link3_1")
async def lin3_1(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("ССЫЛКА НА ФИЛЬМ:\nhttps://kinogo.media/13818-psiho.html\nПриятного просмотра ✨✨✨")

@router.callback_query(F.data == "link3_2")
async def lin3_2(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("ССЫЛКА НА ФИЛЬМ:\nhttps://kinogo.online/filmy/8092-cheljusti.html\nПриятного просмотра ✨✨✨")
    
@router.callback_query(F.data == "link3_3")
async def lin3_3(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("ССЫЛКА НА ФИЛЬМ:\nhttps://kinogo.media/11301-sijanie.html\nПриятного просмотра ✨✨✨")
    
@router.callback_query(F.data == "link4_1")
async def lin4_1(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("ССЫЛКА НА ФИЛЬМ:\nhttps://kinogo.online/filmy/14150-terminator-2-sudnyj-den.html\nПриятного просмотра ✨✨✨")

@router.callback_query(F.data == "link4_2")
async def lin4_2(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("ССЫЛКА НА ФИЛЬМ:\nhttps://kinogo.online/filmy/12278-krepkij-oreshek.html\nПриятного просмотра ✨✨✨")

@router.callback_query(F.data == "link4_3")
async def lin4_3(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("ССЫЛКА НА ФИЛЬМ:\nhttps://kinogo.online/filmy/22442-temnyj-rycar.html\nПриятного просмотра ✨✨✨")

@router.callback_query(F.data == "link5_1")
async def lin5_1(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("ССЫЛКА НА ФИЛЬМ:\nhttps://kinogo-1.net/3159-nachalo-2010-27-06.html\nПриятного просмотра ✨✨✨")

@router.callback_query(F.data == "link5_2")
async def lin5_2(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("ССЫЛКА НА ФИЛЬМ:\nhttps://kinogo.my/films/104-interstellar-2026.html\nПриятного просмотра ✨✨✨")

@router.callback_query(F.data == "link5_3")
async def lin5_3(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("ССЫЛКА НА ФИЛЬМ:\nhttps://kinogo.online/filmy/13855-matrica.html\nПриятного просмотра ✨✨✨")
