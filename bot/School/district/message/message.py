from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types

from config import TOKEN

# some code
from district.school.add import district_school_code, district_school_insert

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



async def district_message(message:types.Message,district_conn,director_conn,conn,district,vote_cb):
    if district[1] == "add school number":
        await district_school_code(message,conn,district_conn,vote_cb)
    elif district[1] == "add school code":
        await district_school_insert(message,conn,district_conn,director_conn,vote_cb)
