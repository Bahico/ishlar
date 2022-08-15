from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types

from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



async def get_contact(message:types.Message,conn,governor_conn,district_conn,director_conn,admin_conn,family_conn,teacher_conn,vote_cb):
    person = conn.execute("select name, text from SAVE where id = (?);",(message.from_user.id,)).fetchall()
    if person:
        person = person[0]
        if person[1] == "contact":
            person = person[0]
            if person == "governor":
                from governor.start.contact import governor_contact
                await governor_contact(message,governor_conn,conn,vote_cb)
            elif person == "district":
                from district.start.contact import district_contact
                await district_contact(message,district_conn,conn,vote_cb)
            elif person == "director":
                from director.start.contact import director_contact
                await director_contact(message,conn,director_conn,vote_cb)
            elif person == "admin":
                from admin.start.contact import admin_contact
                await admin_contact(message, admin_conn, conn, vote_cb)
            elif person == "family":
                from family.start.contact import family_contact
                await family_contact(message, family_conn, conn, vote_cb)
            elif person == "teacher":
                from teacher.start.contact import teacher_contact
                await teacher_contact(message, teacher_conn, conn, vote_cb)