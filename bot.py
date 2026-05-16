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

from link_get import router as link_get_router
from menu import router as menu_router
from apart_handlers import router as apart_router

TOKEN_bot = #YOUR TOKEN 

dp = Dispatcher()

async def main():
    bot=Bot(
        token=TOKEN_bot,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp.include_router(link_get_router)
    dp.include_router(apart_router)
    dp.include_router(menu_router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

