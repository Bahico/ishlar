from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

# some code
from district.menu.menu import district_main_menu
from district.menu.school import district_school_menu
from district.school.add import district_school_number
from district.start.start import district_city, district_code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



async def district_callback(message:types.Message,district_conn,family_conn,conn,vote_cb,callback_query):
    if callback_query["province"] == "stop":
        if callback_query["name"] == "stop":
            await district_main_menu(message, conn, vote_cb)

    elif callback_query["province"] == "start":
        if callback_query["name"] == "governor":
            await district_city(message,district_conn,vote_cb,callback_query)
        elif callback_query["name"] == "city":
            await district_code(message,family_conn,conn,callback_query)

    elif callback_query["province"] == "main menu":
        if callback_query["name"] == "school":
            await district_school_menu(message,vote_cb)
        else:
            pass

    elif callback_query["province"] == "school":
        if callback_query["name"] == "+":
            await district_school_number(message, conn, vote_cb)
        else:
            pass