import json

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

btn1 = KeyboardButton(text="start")
btn2 = KeyboardButton(text="2222")
btn3 = KeyboardButton(text="dsgfdhmh")

menu = ReplyKeyboardMarkup(
    keyboard=[
        [btn1, btn2, btn3]
    ]
)


b1 = KeyboardButton(text="olma")
b2 = KeyboardButton(text="anor")
b3 = KeyboardButton(text="behi")

start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [b1, b2, b3]
    ]
)
