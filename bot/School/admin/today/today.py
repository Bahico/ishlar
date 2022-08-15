from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

#some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def admin_today_number(message:types.Message,admin_conn,class_conn,vote_cb):
    admin_user = admin_conn.execute("select name from USER where id = (?);",(message.from_user.id,)).fetchall()[0][0]
    school = admin_conn.execute("select id from CONN where number = (?);",(admin_user,)).fetchall()[0][0]
    classes = class_conn.execute("select name, number from NUMBER where id = (?);",(school,)).fetchall()
    markup = InlineKeyboardMarkup(row_width=2)
    for i in classes:
        markup.insert(InlineKeyboardButton(text=i[0],callback_data=vote_cb.new(name="number",province="today",city=i[1],school="None",tur="None",clas="None",action="admin")))
    await bot.send_message(message.from_user.id,"Nechinchi sinf davomatini tekshirmoqchisiz?",reply_markup=markup)

async def admin_today_name(message:types.Message,class_conn,vote_cb,callback_query):
    classes = class_conn.execute("select name, number from NAME where id = (?);",(callback_query["city"],)).fetchall()
    markup = InlineKeyboardMarkup(row_width=2)
    for i in classes:
        markup.insert(InlineKeyboardButton(text=i[0],callback_data=vote_cb.new(name="name",province="today",city=i[1],school="None",tur="None",clas="None",action="admin")))
    await bot.send_message(message.from_user.id,"Qaysi sinf davomatini tekshirmoqchisiz?",reply_markup=markup)

async def admin_today_student(message:types.Message,student_conn,vote_cb,callback_query):
    students = student_conn.execute("select first_name, last_name, number from CONN where id = (?);",(callback_query["city"],)).fetchall()
    markup = InlineKeyboardMarkup(row_width=2)
    for i in students:
        markup.insert(InlineKeyboardButton(text=f"{i[0]} {i[1]}",callback_data=vote_cb.new(name="student",province="today",city=i[2],school="None",tur="None",clas="None",action="admin")))
    await bot.send_message(message.from_user.id,"Kelmagan o'quvchilarni tanlang",reply_markup=markup)

