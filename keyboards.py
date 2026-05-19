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

menu_key = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text="Да, готов", callback_data="get_yes_menu"),
            InlineKeyboardButton(text="Нет", callback_data="get_no_menu")
        ]
    ]
)

def fav_genre_key():
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text="ВЕСТЕРН 🤠🏜️"))
    builder.add(types.KeyboardButton(text="КОМЕДИЯ 🤣"))
    builder.add(types.KeyboardButton(text="УЖАСЫ 👻"))
    builder.add(types.KeyboardButton(text="БОЕВИК 🔫"))
    builder.add(types.KeyboardButton(text="НАУЧНАЯ ФАНТАСТИКА 🚀"))
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)

chek_1 = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text="Взглянуть 👍", callback_data="get_chek_1")
        ]
    ]
)

chek_2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Взглянуть 👍", callback_data="get_chek_2")
        ]
    ]
)

chek_3 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Взглянуть 👍", callback_data="get_chek_3")
        ]
    ]
)

chek_4 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Взглянуть 👍", callback_data="get_chek_4")
        ]
    ]
)

chek_5 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Взглянуть 👍", callback_data="get_chek_5")
        ]
    ]
)

choice_key = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text="Да, готов", callback_data="get_yes_ch"),
            InlineKeyboardButton(text="Нет", callback_data="get_no_ch")
        ]
    ]
)


def fav_genre_key_1():
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text="Вестерн 🤠🏜️"))
    builder.add(types.KeyboardButton(text="Комедия 🤣"))
    builder.add(types.KeyboardButton(text="Ужасы 👻"))
    builder.add(types.KeyboardButton(text="Боевик 🔫"))
    builder.add(types.KeyboardButton(text="Научная фантастика 🚀"))
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)

def menu_do():
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text="Вернуться ♻️"))
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)

linkme1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Получить ссылку на фильм ▶️", callback_data="link1_1"),
            InlineKeyboardButton(text="Добавить в избранное 🔖", callback_data="get_fav_1_1")
        ]
    ]
)

linkme2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Получить ссылку на фильм ▶️", callback_data="link1_2"),
            InlineKeyboardButton(text="Добавить в избранное 🔖", callback_data="get_fav_1_2")
        ]
    ]
)

linkme3 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Получить ссылку на фильм ▶️", callback_data="link1_3"),
            InlineKeyboardButton(text="Добавить в избранное 🔖", callback_data="get_fav_1_3")
        ]
    ]
)


linkme4 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Получить ссылку на фильм ▶️", callback_data="link2_1"),
            InlineKeyboardButton(text="Добавить в избранное 🔖", callback_data="get_fav_2_1")
        ]
    ]
)


linkme5 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Получить ссылку на фильм ▶️", callback_data="link2_2"),
            InlineKeyboardButton(text="Добавить в избранное 🔖", callback_data="get_fav_2_2")
        ]
    ]
)


linkme6 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Получить ссылку на фильм ▶️", callback_data="link2_3"),
            InlineKeyboardButton(text="Добавить в избранное 🔖", callback_data="get_fav_2_3")
        ]
    ]
)

linkme7 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Получить ссылку на фильм ▶️", callback_data="link3_1"),
            InlineKeyboardButton(text="Добавить в избранное 🔖", callback_data="get_fav_3_1")
        ]
    ]
)

linkme8 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Получить ссылку на фильм ▶️", callback_data="link3_2"),
            InlineKeyboardButton(text="Добавить в избранное 🔖", callback_data="get_fav_3_2")
        ]
    ]
)

linkme9 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Получить ссылку на фильм ▶️", callback_data="link3_3"),
            InlineKeyboardButton(text="Добавить в избранное 🔖", callback_data="get_fav_3_3")
        ]
    ]
)

linkme10 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Получить ссылку на фильм ▶️", callback_data="link4_1"),
            InlineKeyboardButton(text="Добавить в избранное 🔖", callback_data="get_fav_4_1")
        ]
    ]
)

linkme11 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Получить ссылку на фильм ▶️", callback_data="link4_2"),
            InlineKeyboardButton(text="Добавить в избранное 🔖", callback_data="get_fav_4_2")
        ]
    ]
)

linkme12 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Получить ссылку на фильм ▶️", callback_data="link4_3"),
            InlineKeyboardButton(text="Добавить в избранное 🔖", callback_data="get_fav_4_3")
        ]
    ]
)

linkme13 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Получить ссылку на фильм ▶️", callback_data="link5_1"),
            InlineKeyboardButton(text="Добавить в избранное 🔖", callback_data="get_fav_5_1")
        ]
    ]
)

linkme14 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Получить ссылку на фильм ▶️", callback_data="link5_2"),
            InlineKeyboardButton(text="Добавить в избранное 🔖", callback_data="get_fav_5_2")
        ]
    ]
)

linkme15 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Получить ссылку на фильм ▶️", callback_data="link5_3"),
            InlineKeyboardButton(text="Добавить в избранное 🔖", callback_data="get_fav_5_3")
        ]
    ]
)








