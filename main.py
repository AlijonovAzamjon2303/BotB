import asyncio
import json
import logging
import sys

from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from config import TOKEN
from keyboards import menu, start_menu


dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!", reply_markup=menu)

@dp.message(F.text.isdigit())
async def get_user(message: Message):
    if message.text.isdigit():
        with open("users.json", "r") as file:
            users = json.load(file)
        if message.text in users:
            user = users[message.text]
            answer = f"Ismi : {user['name']}, yoshi : {user['age']}"
            await message.answer(answer)
        else:
            await message.answer(f"{message.text} id li user yo'q")

@dp.message(F.text == "start")
async def show_start_menu(message: Message):
    await message.answer("Quyidagilardan birini tanlashingiz mumkin", reply_markup=start_menu)

@dp.message()
async def echo_handler(message: Message) -> None:
    if "salom" in message.text.lower():
        await message.answer("Va alaykum assalom")
    else:
        await message.answer(message.text)


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())