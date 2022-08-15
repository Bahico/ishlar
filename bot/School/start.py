from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types

from admin.menu.menu import admin_main_menu
from config import TOKEN

# some code
from director.menu.menu import director_main_menu
from district.menu.menu import district_main_menu
from family.menu.menu import family_main_menu
from family.start.start import family_governor
from governor.menu.main_menu import governor_main_menu
from teacher.menu.menu import teacher_main_menu

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def get_start(message:types.Message,governor_conn,district_conn,director_conn,class_conn,conn,vote_cb):
    person = conn.execute("select name from SAVE where id = (?);",(message.from_user.id,)).fetchall()
    if not person:
        await family_governor(message, governor_conn, district_conn, director_conn, class_conn, vote_cb)
    elif person[0][0] == "family":
        await family_main_menu(message, conn, vote_cb)
    elif person[0][0] == "governor":
        await governor_main_menu(message, conn, vote_cb)
    elif person[0][0] == "district":
        await district_main_menu(message, conn, vote_cb)
    elif person[0][0] == "director":
        await director_main_menu(message, conn, vote_cb)
    elif person[0][0] == "admin":
        await admin_main_menu(message, conn, vote_cb)
    elif person[0][0] == "teacher":
        await teacher_main_menu(message, conn, vote_cb)