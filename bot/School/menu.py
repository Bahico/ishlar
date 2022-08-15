from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types

from admin.menu.menu import admin_main_menu
from config import TOKEN

# some code
from director.menu.menu import director_main_menu
from district.menu.menu import district_main_menu
from family.menu.menu import family_main_menu
from governor.menu.main_menu import governor_main_menu
from teacher.menu.menu import teacher_main_menu

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def get_menu(message:types.Message,conn,vote_cb):
    await message.delete()
    person = conn.execute("select name from SAVE where id = (?);",(message.from_user.id,)).fetchall()
    if person:
        person = person[0][0]
        if person == "governor":
            await governor_main_menu(message, conn, vote_cb)
        elif person == "district":
            await district_main_menu(message, conn, vote_cb)
        elif person == "director":
            await director_main_menu(message, conn, vote_cb)
        elif person == "admin":
            await admin_main_menu(message, conn, vote_cb)
        elif person == "teacher":
            await teacher_main_menu(message, conn, vote_cb)
        elif person == "family":
            await family_main_menu(message, conn, vote_cb)