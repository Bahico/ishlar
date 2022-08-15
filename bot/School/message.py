from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types

from admin.message.message import admin_message
from config import TOKEN

# some code
from director.message import director_message
from district.message.message import district_message
from family.message.message import family_message
from governor.message.message import governor_message
from teacher.message.message import teacher_message

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def get_message(message:types.Message,governor,governor_conn,district_conn,director_conn,admin_conn,family_conn,student_conn,teacher_conn,class_conn,conn,vote_cb):
    await message.delete()
    if message.from_user.id == 5012085359:
        if governor and governor[0] is True:
            from main import governor
            governor.clear()
            admin = conn.execute("select id from ADMIN;").fetchall()
            for i in admin:
                if i[0] is not None:
                    await bot.send_message(i[0],message.text)


        elif governor and governor[0] == "add_governor":
            from main import governor
            governor.clear()
            typ = message.text
            typ = typ.split(',')
            governor_conn.execute("insert into CONN(name,code) values (?,?);", (typ[0], typ[1],))
            await bot.send_message(message.from_user.id,f"Qabul qilindi!\n{typ[0]} viloyati \ncode:{typ[1]}")


    person = conn.execute("select name, text from SAVE where ID = (?) LIMIT 1 ;", (message.from_user.id,)).fetchall()
    if person:
        person = person[0]
         #  ------FAMILY MESSAGE ---------
        if person[0] == "family":
            await family_message(message,governor_conn,district_conn,director_conn,admin_conn,family_conn,student_conn,teacher_conn,conn,vote_cb,person)

        #   --------TEACHER MESSAGE ---------
        elif person[0] == "teacher":
            await teacher_message(message, teacher_conn, conn, vote_cb, person)

        #      -------DIRECTOR MESSAGE -----
        elif person[0] == "director":
            await director_message(message,director_conn,admin_conn,conn,vote_cb,person)

        #    ---- ADMIN MESSAGE-------
        elif person[0] == "admin":
            await admin_message(message,admin_conn,student_conn,teacher_conn,class_conn,conn,person,vote_cb)

        #   -----GOVERNOR MESSAGE-----
        elif person[0] == "governor":
            await governor_message(message,governor_conn,district_conn,conn,person,vote_cb)

        #  -----DISTRICT GOVERNOR MESSAGE ----
        elif person[0] == "district":
            await district_message(message,district_conn,director_conn,conn,person,vote_cb)
