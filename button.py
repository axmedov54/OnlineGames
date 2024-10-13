from aiogram.types import WebAppInfo,InlineKeyboardButton,InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

menyu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Shaxmat ♟", web_app=WebAppInfo(url='https://www.chess.com/play/online')),InlineKeyboardButton(text="Shashka ♟", web_app=WebAppInfo(url='https://checkers.online/play'))],
        [InlineKeyboardButton(text="Subway Surfers 🚈", web_app=WebAppInfo(url='https://subway-surfers.org/las-vegas/')),InlineKeyboardButton(text="LEVEL DEVIL 😈", web_app=WebAppInfo(url='https://poki.com/uz/g/level-devil#fullscreen'))],
        [InlineKeyboardButton(text="FOOTBALL LEGENDS ⚽", web_app=WebAppInfo(url='https://poki.com/uz/g/football-legends#fullscreen')),InlineKeyboardButton(text="THE SPEAR STICKMAN ", web_app=WebAppInfo(url='https://poki.com/uz/g/the-spear-stickman#fullscreen'))],
        [InlineKeyboardButton(text="WAR OF STICKS ", web_app=WebAppInfo(url='https://poki.com/uz/g/war-of-sticks'))]
    ]

)