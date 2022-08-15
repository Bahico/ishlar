from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types

from config import TOKEN

# some code
from governor.disrtict.add.start import governor_district_name
from governor.menu.district import governor_district_menu
from governor.menu.main_menu import governor_main_menu
from governor.start.start import governor_province

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



async def governor_callback(message:types.Message,family_conn,conn,vote_cb,callback_query):
    if callback_query["province"] == "stop":
        if callback_query["name"] == "stop":
            await governor_main_menu(message, conn, vote_cb)
    elif callback_query["province"] == "start":
        if callback_query["name"] == "governor":
            await governor_province(message,family_conn,conn,callback_query)

    elif callback_query["province"] == "main menu":
        if callback_query["name"] == "district":
            await governor_district_menu(message,vote_cb)
        else:
            pass

    elif callback_query["province"] == "district":
        if callback_query["name"] == "+":
            await governor_district_name(message,conn,vote_cb)
        else:
            pass