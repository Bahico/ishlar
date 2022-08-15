from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

# some code
from teacher.fan.fan import teacher_fan_insert
from teacher.menu.menu import teacher_main_menu
from teacher.menu.settings import teacher_edit_code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



async def teacher_message(message:types.Message,teacher_conn,conn,vote_cb,person):
    print(message.text)
    if person[1] == "add fan":
        await teacher_fan_insert(message, teacher_conn, conn, vote_cb)
    elif person[1] == "edit code":
        await teacher_edit_code(message, teacher_conn, conn, vote_cb)