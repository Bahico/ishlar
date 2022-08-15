from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types

from admin.start.start import admin_code
from config import TOKEN

# some code
from director.start.start import director_start_insert
from district.start.start import district_insert
from family.start.start import family_insert, family_add_children
from governor.start.start import governor_code
from teacher.start.start import teacher_insert

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def family_message(message: types.Message, governor_conn, district_conn, director_conn, admin_conn, family_conn, student_conn, teacher_conn, conn, vote_cb, family):
    if family[1] == "governor":
        await governor_code(message, family_conn, governor_conn, conn)
    elif family[1] == "district":
        await district_insert(message,conn,family_conn,district_conn)
    elif family[1] == "director":
        await director_start_insert(message, conn, family_conn, director_conn)
    elif family[1] == "admin":
        await admin_code(message, admin_conn, family_conn,conn)
    elif family[1] == "code":
        await family_insert(message, student_conn, family_conn, director_conn, conn)
    elif family[1] == "code_":
        await family_add_children(message, student_conn, family_conn, director_conn, conn, vote_cb)
    elif family[1] == "teacher":
        await teacher_insert(message, family_conn, teacher_conn, conn)