import sqlite3

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from aiogram.utils.callback_data import CallbackData

from admin.callback.callback import admin_callback
from admin.start.start import admin_login
from config import TOKEN, governor
from contact import get_contact
from director.callback.callback import director_callback
from director.start.start import director_start_province
from district.callback import district_callback
from district.start.start import district_province
from family.callback.callback import family_callback
from governor.callback import governor_callback
from governor.start.start import governor_governor
from logout import get_logout
from menu import get_menu
from message import get_message
from start import get_start
from teacher.callback.callback import teacher_callback
from teacher.start.start import teacher_province

conn = sqlite3.connect('conn.db')
admin_conn = sqlite3.connect("admin/admin.db")
attend_conn = sqlite3.connect("attend/attend.db")
director_conn = sqlite3.connect("director/school.db")
family_conn = sqlite3.connect("family/family.db")
governor_conn = sqlite3.connect("governor/governor.db")
district_conn = sqlite3.connect("district/district.db")
student_conn = sqlite3.connect("student/student.db")
teacher_conn = sqlite3.connect("teacher/teacher.db")
class_conn = sqlite3.connect("student/class_conn.db")


# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



vote_cb = CallbackData('vote', 'name', 'province', 'city', 'school', 'tur', 'clas', 'action')  # post:<action>:<amount>



#   -------FAMILY START------
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await get_start(message,governor_conn,district_conn,director_conn,class_conn,conn,vote_cb)
    await bot.delete_message(message.from_user.id, message.message_id)


#   -------GOVERNOR START-------
@dp.message_handler(commands=["governor"])
async def governor_start(message: types.Message):
    await governor_governor(message,governor_conn,family_conn,conn,vote_cb)
    await message.delete()


#   -----DISTRICT START-------
@dp.message_handler(commands=["district_governor"])
async def district_start(message: types.Message):
    await district_province(message, district_conn, governor_conn, family_conn, conn, vote_cb)
    await message.delete()



#   -------TEACHER START-------
@dp.message_handler(commands=['teacher'])
async def teacher_start(message: types.Message):
    await teacher_province(message, teacher_conn, governor_conn,conn,vote_cb)
    await bot.delete_message(message.from_user.id, message.message_id)


#   -------DIRECTOR START -------
@dp.message_handler(commands=['director'])
async def director_start(message: types.Message):
    await director_start_province(message, director_conn, governor_conn, conn, vote_cb)
    await bot.delete_message(message.from_user.id, message.message_id)

#       --------ADMIN START------
@dp.message_handler(commands=['admin'])
async def admin_start(message: types.Message):
    await admin_login(message, admin_conn, family_conn,conn, vote_cb)
    await message.delete()


#  -------CONTACT-------
@dp.message_handler(content_types=['contact'])
async def contact(message:types.Message):
    await get_contact(message,conn,governor_conn,district_conn,director_conn,admin_conn,family_conn,teacher_conn,vote_cb)


#   -------CITY -------
@dp.callback_query_handler(vote_cb.filter(action='family'))
async def family_city(message: types.Message, callback_data: dict):
    await family_callback(message,governor_conn,district_conn,director_conn,class_conn,student_conn,family_conn,conn,vote_cb,callback_data)
    try:await bot.delete_message(message.from_user.id,message.message.message_id)
    except:pass
    conn.commit()
    admin_conn.commit()
    attend_conn.commit()
    director_conn.commit()
    district_conn.commit()
    family_conn.commit()
    governor_conn.commit()
    student_conn.commit()
    teacher_conn.commit()
    class_conn.commit()


#  -----------TEACHER CALLBACK ----------
@dp.callback_query_handler(vote_cb.filter(action="teacher"))
async def get_teacher_city(message: types.Message, callback_data: dict):
    await teacher_callback(message,district_conn,director_conn,teacher_conn,family_conn,class_conn,attend_conn,student_conn,conn,vote_cb,callback_data)
    try: await bot.delete_message(message.from_user.id,message.message.message_id)
    except: pass
    conn.commit()
    admin_conn.commit()
    attend_conn.commit()
    director_conn.commit()
    district_conn.commit()
    family_conn.commit()
    governor_conn.commit()
    student_conn.commit()
    teacher_conn.commit()
    class_conn.commit()



#    ------DIRECTOR CITY------
@dp.callback_query_handler(vote_cb.filter(action="director"))
async def director_city(message: types.Message, callback_data: dict):
    await director_callback(message,district_conn,director_conn,family_conn,attend_conn,conn,vote_cb,callback_data)
    try:await bot.delete_message(message.from_user.id,message.message.message_id)
    except:pass
    conn.commit()
    admin_conn.commit()
    attend_conn.commit()
    director_conn.commit()
    district_conn.commit()
    family_conn.commit()
    governor_conn.commit()
    student_conn.commit()
    teacher_conn.commit()
    class_conn.commit()


#  -------ADMIN CITY------
@dp.callback_query_handler(vote_cb.filter(action="admin"))
async def admin_city(message: types.Message, callback_data: dict):
    await admin_callback(message,admin_conn,class_conn,attend_conn,student_conn,teacher_conn,conn,vote_cb,callback_data)
    try:await bot.delete_message(message.from_user.id,message.message.message_id)
    except:pass
    conn.commit()
    admin_conn.commit()
    attend_conn.commit()
    director_conn.commit()
    district_conn.commit()
    family_conn.commit()
    governor_conn.commit()
    student_conn.commit()
    teacher_conn.commit()
    class_conn.commit()




#    ------DISTRICT CALLBACK ------
@dp.callback_query_handler(vote_cb.filter(action="district"))
async def district_city(message: types.Message, callback_data: dict):
    try:await bot.delete_message(message.from_user.id,message.message.message_id)
    except:pass
    await district_callback(message,district_conn,family_conn,conn,vote_cb,callback_data)
    conn.commit()
    admin_conn.commit()
    attend_conn.commit()
    director_conn.commit()
    district_conn.commit()
    family_conn.commit()
    governor_conn.commit()
    student_conn.commit()
    teacher_conn.commit()
    class_conn.commit()



#   -----GOVERNOR CALLBACK -------
@dp.callback_query_handler(vote_cb.filter(action="governor"))
async def governor_city(message: types.Message, callback_data: dict):
    await governor_callback(message,family_conn,conn,vote_cb,callback_data)
    try:await bot.delete_message(message.from_user.id,message.message.message_id)
    except:pass
    conn.commit()
    admin_conn.commit()
    attend_conn.commit()
    director_conn.commit()
    district_conn.commit()
    family_conn.commit()
    governor_conn.commit()
    student_conn.commit()
    teacher_conn.commit()
    class_conn.commit()




#   -------HELP------
@dp.message_handler(commands=['help'])
async def get_help(message: types.Message):
    await bot.send_message(message.from_user.id,"Assalomu aleykum bu botni muaillifi Bahodrjon Ikromov \nAgar botda xatoliklar bolayotgan bo'lsa yoki murojaatlar bo'lsa\n👉@baxtlimanjudajuda tugmasini bosib men bilan bog'lanishingiz mumkin")


#  My message
@dp.message_handler(commands=['add_governor'])
async def add_governor(message: types.Message):
    global governor
    if message.chat.id == 5012085359:
        governor.append("add_governor")
        await bot.send_message(message.from_user.id,"Viloyat qo'shish uchun\nShu ko'rinishida yozing: Viloyat,code")
    else:
        await bot.send_message(message.from_user.id, "Siz Bahodirjon emassiz!")


@dp.message_handler(commands=['del_governor'])
async def del_governor(message: types.Message):
    global governor
    if message.chat.id == 5012085359:
        governor = conn.execute("select * from GOVERNOR;").fetchall()
        Governor = InlineKeyboardMarkup(resize_keyboard=True)
        for i in governor:
            Governor.add(InlineKeyboardButton(text=i))
        await bot.send_message(message.from_user.id, "hoz")
    else:
        await bot.send_message(message.from_user.id, "Siz Bahodirjon emassiz")


@dp.message_handler(commands=['menu'])
async def all_menu(message: types.Message):
    await get_menu(message,conn,vote_cb)


# @dp.message_handler(content_types=['photo'])
# async def get_photo(message: types.Message):
#     if message.from_user.id == 5012085359:
#         await bot.send_photo(message.from_user.id,message.photo[0].file_id,message.text)


@dp.message_handler(commands=['send'])
async def get_send(message:types.Message):
    global I_
    I_ = True
    await bot.delete_message(message.from_user.id,message.message_id)


@dp.message_handler(commands=['logout'])
async def logout(message:types.Message):
    await get_logout(message,governor_conn,district_conn,director_conn,admin_conn,teacher_conn,family_conn,conn)


#   -----ALL MESSAGE------

@dp.message_handler()
async def index(message: types.Message):
    global governor
    await get_message(message,governor,governor_conn,district_conn,director_conn,admin_conn,family_conn,student_conn,teacher_conn,class_conn,conn,vote_cb)
    conn.commit()
    admin_conn.commit()
    attend_conn.commit()
    director_conn.commit()
    district_conn.commit()
    family_conn.commit()
    governor_conn.commit()
    student_conn.commit()
    teacher_conn.commit()
    class_conn.commit()



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)