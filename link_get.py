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
