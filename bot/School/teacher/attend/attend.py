import datetime

from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

# some code
from teacher.menu.menu import teacher_main_menu

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



async def teacher_attend_number(message:types.Message,teacher_conn,class_conn,attend_conn,vote_cb):
    school_id = teacher_conn.execute("select name from USER where id = (?);",(message.from_user.id,)).fetchall()[0][0]
    school_id = teacher_conn.execute("select id from CONN where number = (?);",(school_id,)).fetchall()[0][0]
    classes = class_conn.execute("select name, number from NUMBER where id = (?);",(school_id,)).fetchall()
    markup = InlineKeyboardMarkup(reply_markup=True,row_width=3)
    for i in sorted(classes):
        markup.insert(InlineKeyboardButton(text=str(i[0]),callback_data=vote_cb.new(name="class number", province="attend",city=i[1], school="", tur="None",clas=school_id, action="teacher")))
    await bot.send_message(message.from_user.id,"Nechinchi sinfga darsga kirdingiz?",reply_markup=markup)
    date = datetime.datetime.now().strftime("%x").split("/"); date = date[0]+"/"+date[2]
    school = attend_conn.execute("select * from SCHOOL where id = (?) and date = (?);",(school_id,date)).fetchall()
    if not school:
        attend_conn.execute("insert into SCHOOL(id,date) values (?,?);",(school_id,date))


async def teacher_attend_name(message:types.Message,class_conn,vote_cb,callback_query):
    classes = class_conn.execute("select name, number from NAME where id = (?);",(callback_query["city"],)).fetchall()
    markup = InlineKeyboardMarkup(row_width=2,reply_markup=True)
    for i in classes:
        markup.insert(InlineKeyboardButton(text=i[0],callback_data=vote_cb.new(name="class name", province="attend",city=i[1], school="", tur="None",clas="", action="teacher")))
    markup.add(InlineKeyboardButton(text="⬅️ORTGA",callback_data=vote_cb.new(name="attend", province="main menu",city="", school="", tur="None",clas="", action="teacher")))
    await bot.send_message(message.from_user.id,"Qaysi sinfga darsga kirdingiz?",reply_markup=markup)

async def teacher_attend_lesson(message:types.Message,attend_conn,vote_cb,callback_query):
    lesson = attend_conn.execute("select lesson1,lesson2,lesson3,lesson4,lesson5,lesson6,lesson7 from CLASS where id = (?);",(callback_query["city"],)).fetchall()
    markup = InlineKeyboardMarkup(row_width=3,reply_markup=True)
    if lesson:
        son = 0
        lesson = lesson[0]
        for i in lesson:
            son += 1
            if i is None:
                markup.insert(InlineKeyboardButton(text=str(son),callback_data=vote_cb.new(name="lesson", province="attend",city=son, school=callback_query["city"], tur="",clas="", action="teacher")))
            else:
                markup.insert(InlineKeyboardButton(text="✅ "+str(son),callback_data=vote_cb.new(name="lesson", province="attend",city=son, school=callback_query["city"], tur="",clas="", action="teacher")))
        await bot.send_message(message.from_user.id,"Nechinchi soat darsni o'tyapsiz?",reply_markup=markup)
    else:
        for i in range(1,7):
            markup.insert(InlineKeyboardButton(text=str(i),callback_data=vote_cb.new(name="lesson", province="attend",city=i, school=callback_query["city"], tur="",clas="", action="teacher")))
        await bot.send_message(message.from_user.id,"Nechinchi soat darsga kirdingiz?",reply_markup=markup)

async def teacher_attend_arr(message:types.Message,student_conn,attend_conn,vote_cb,callback_query):
    date = datetime.datetime.now().strftime("%x").split("/"); date = date[0]+"/"+date[2]+"/"+date[1]
    class_arr = student_conn.execute("select first_name, last_name, number from CONN where id = (?);",(callback_query["school"],)).fetchall()
    markup = InlineKeyboardMarkup(row_width=2,reply_markup=True)
    for i in class_arr:
        student = attend_conn.execute("select name, lesson from STUDENT where id = (?) and date = (?);",(i[2],date)).fetchall()
        if len(student) == 1 and student[0][0] != "escape": markup.insert(InlineKeyboardButton(text=f"🔴 {i[0]} {i[1]}",callback_data=vote_cb.new(name="student_", province="attend",city=i[2], school="all", tur=callback_query["school"],clas=callback_query["clas"], action="teacher")))
        elif student and student[0][0] == "escape":
            son = 0
            for student in student:
                if str(student[1]) == callback_query["city"]:
                    son = 1
            if son == 1: markup.insert(InlineKeyboardButton(text=f"🟡 {i[0]} {i[1]}",callback_data=vote_cb.new(name="student_", province="attend",city=i[2], school=callback_query["city"], tur=callback_query["school"],clas="", action="teacher")))
            else: markup.insert(InlineKeyboardButton(text=f"{i[0]} {i[1]}",callback_data=vote_cb.new(name="student", province="attend",city=i[2], school=callback_query["city"], tur=callback_query["school"],clas="", action="teacher")))
        else: markup.insert(InlineKeyboardButton(text=f"{i[0]} {i[1]}",callback_data=vote_cb.new(name="student", province="attend",city=i[2], school=callback_query["city"], tur=callback_query["school"],clas="", action="teacher")))
    markup.add(InlineKeyboardButton(text="✅ Tugatish",callback_data=vote_cb.new(name="finish", province="attend",city=callback_query["city"], school=callback_query["school"], tur="",clas="", action="teacher")))
    await bot.send_message(message.from_user.id,"Darsda yo'q o'quvchilarni tanlang",reply_markup=markup)

async def teacher_attend_del(message:types.Message,teacher_conn,student_conn,attend_conn,vote_cb,callback_query):
    date = datetime.datetime.now().strftime("%x").split("/"); school_date = date[0]+"/"+date[2]; date = date[0]+"/"+date[2]+"/"+date[1]
    attend_conn.execute("insert into STUDENT(id,date,name,lesson,school) values (?,?,?,?,?);",(callback_query["city"],date,"escape",callback_query["school"],callback_query["clas"]))
    callback_query["city"] = callback_query["school"]; callback_query["school"] = callback_query["tur"]
    await teacher_attend_arr(message, student_conn, attend_conn, vote_cb, callback_query)
    school_id = teacher_conn.execute("select name from USER where id = (?);",(message.from_user.id,)).fetchall()[0][0]
    school_id = teacher_conn.execute("select id from CONN where number = (?);",(school_id,)).fetchall()[0][0]
    escape = attend_conn.execute("select escape_ from SCHOOL where id = (?) and date = (?);",(school_id,school_date)).fetchall()[0][0]
    if escape is None:
        attend_conn.execute("update SCHOOL set escape_ = 1 where id = (?) and date = (?);",(school_id,school_date))
    else:
        attend_conn.execute("update SCHOOL set escape_ = (?) where id = (?) and date = (?);",(escape+1,school_id,school_date))

async def teacher_attend_del_(message:types.Message,teacher_conn,student_conn,attend_conn,vote_cb,callback_query):
    date = datetime.datetime.now().strftime("%x").split("/"); school_date = date[0]+"/"+date[2]; date = date[0]+"/"+date[2]+"/"+date[1]
    if callback_query["school"] != "all": attend_conn.execute("delete from STUDENT where id = (?) and date = (?) and name = (?) and lesson = (?);",(callback_query["city"],date,"escape",callback_query["school"]))
    else: attend_conn.execute("delete from STUDENT where id = (?) and date = (?);",(callback_query["city"],date))
    callback_query["city"] = callback_query["school"]; callback_query["school"] = callback_query["tur"]
    await teacher_attend_arr(message, student_conn, attend_conn, vote_cb, callback_query)
    school_id = teacher_conn.execute("select name from USER where id = (?);",(message.from_user.id,)).fetchall()[0][0]
    school_id = teacher_conn.execute("select id from CONN where number = (?);",(school_id,)).fetchall()[0][0]
    escape = attend_conn.execute("select escape_ from SCHOOL where id = (?) and date = (?);",(school_id,school_date)).fetchall()[0][0]
    if escape-1 <= 0:
        attend_conn.execute("update SCHOOL set escape_ = NULL where id = (?) and date = (?);",(school_id,school_date))
    else:
        attend_conn.execute("update SCHOOL set escape_ = (?) where id = (?) and date = (?);",(escape-1,school_id,school_date))


async def teacher_attend_fan(message:types.Message,teacher_conn,vote_cb,callback_query):
    fans = teacher_conn.execute("select name, number from FAN where id = (?);",(message.from_user.id,)).fetchall()
    markup = InlineKeyboardMarkup(row_width=2)
    for i in fans:
        fan = teacher_conn.execute("select name from FAN_CONN where number = (?);",(i[0],)).fetchall()[0][0]
        markup.insert(InlineKeyboardButton(text=fan,callback_data=vote_cb.new(name="fan", province="attend",city=i[1], school=callback_query["city"], tur=callback_query["school"],clas="", action="teacher")))
    markup.add(InlineKeyboardButton(text="⬅️ ORTGA",callback_data=vote_cb.new(name="lesson", province="attend",city=callback_query["city"], school=callback_query["school"], tur="",clas="", action="teacher")))
    await bot.send_message(message.from_user.id,"Qaysi fandan tars o'tyapsiz?",reply_markup=markup)

async def teacher_attend_finish(message:types.Message,attend_conn,conn,vote_cb,callback_query):
    date = datetime.datetime.now().strftime("%x").split("/"); date = date[0]+"/"+date[2]+"/"+date[1]
    clas = attend_conn.execute("select * from CLASS where id = (?) and date = (?);",(callback_query["school"],date)).fetchall()
    if clas: attend_conn.execute(f"update CLASS set lesson{str(callback_query['school'])} = (?) where id = (?) and date = (?);",(callback_query["city"],callback_query["tur"],date))
    else: attend_conn.execute(f"insert into CLASS(id,date,lesson{str(callback_query['school'])}) values (?,?,?);",(callback_query["tur"],date,callback_query["city"]))
    await teacher_main_menu(message,conn,vote_cb)