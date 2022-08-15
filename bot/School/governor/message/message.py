from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types

from config import TOKEN

# some code
from governor.disrtict.add.start import governor_district_code, governor_district_insert

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



async def governor_message(message:types.Message,governor_conn,district_conn,conn,governor,vote_cb):
    if governor[1] == "add district name":
        await governor_district_code(message,conn,governor_conn)
    elif governor[1] == "add district code":
        await governor_district_insert(message,conn,governor_conn,district_conn,vote_cb)