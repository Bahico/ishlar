import datetime

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

#some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



async def attend_today_number(message:types.Message,admin_conn,attend_conn,class_conn,vote_cb):
    date = datetime.datetime.now().strftime("%x").split("/");school_date = date[0]+"/"+date[2]; date = date[0]+"/"+date[2]+"/"+date[1]
    admin = admin_conn.execute("select name from USER where id = (?);",(message.from_user.id,)).fetchall()[0][0]
    admin = admin_conn.execute("select id from CONN where number = (?);",(admin,)).fetchall()[0][0]
    attend = attend_conn.execute("select * from school where id = (?) and date = (?);",(admin,school_date)).fetchall()
    classes = class_conn.execute("select name, number, date from NUMBER where id = (?);",(admin,)).fetchall()
    print(attend)
    if not attend:
        attend_conn.execute("insert into school(id,date) values (?,?);",(admin,school_date))
    markup = InlineKeyboardMarkup(row_width=3)
    for i in sorted(classes):
        if i[2] == date:
             markup.insert(InlineKeyboardButton(text="✅ "+str(i[0]),callback_data=vote_cb.new(name="class number",province="attend",city=i[1],school=admin,tur="None",clas="None",action="admin")))
        else:
            markup.insert(InlineKeyboardButton(text=i[0],callback_data=vote_cb.new(name="class number",province="attend",city=i[1],school=admin,tur="None",clas="None",action="admin")))
    await bot.send_message(message.from_user.id,"Nechinchi sinf davomatini tekshirmoqchisiz?",reply_markup=markup)

async def attend_today_name(message:types.Message,class_conn,vote_cb,callback_query):
    date = datetime.datetime.now().strftime("%x").split("/"); date = date[0]+"/"+date[2]+"/"+date[1]
    classes = class_conn.execute("select name, number, date from NAME where id = (?);",(callback_query["city"],)).fetchall()
    markup = InlineKeyboardMarkup(row_width=2)
    for i in classes:
        if i[2] == date:
            markup.insert(InlineKeyboardButton(text="✅ "+i[0],callback_data=vote_cb.new(name="class name",province="attend",city=i[1],school=callback_query["school"],tur="True",clas=callback_query["city"],action="admin")))
        else:
            markup.insert(InlineKeyboardButton(text=i[0],callback_data=vote_cb.new(name="class name",province="attend",city=i[1],school=callback_query["school"],tur="None",clas=callback_query["city"],action="admin")))
    markup.add(InlineKeyboardButton(text="⬅️ ORTGA",callback_data=vote_cb.new(name="attend",province="main menu",city="",school=callback_query["school"],tur="None",clas=callback_query["city"],action="admin")))
    await bot.send_message(message.from_user.id,"Qaysi sinfni davomatini tekshirmoqchisiz?",reply_markup=markup)

async def attend_today_arr(message:types.Message,student_conn,attend_conn,vote_cb,callback_query):
    date = datetime.datetime.now().strftime("%x").split("/"); date = date[0]+"/"+date[2]+"/"+date[1]
    students = student_conn.execute("select first_name, last_name, number from CONN where id = (?);",(callback_query["city"],)).fetchall()
    markup = InlineKeyboardMarkup(row_width=2)
    for i in students:
        student = attend_conn.execute("select name from STUDENT where id = (?) and date = (?);",(i[2],date)).fetchall()
        if student and student[0][0] == "no reason":
            markup.insert(InlineKeyboardButton(text=f"🔴 {i[0]} {i[1]}",callback_data=vote_cb.new(name="student_",province="attend",city=i[2],school=callback_query["school"],tur=callback_query["city"],clas=callback_query["clas"],action="admin")))
        elif student and student[0][0] == "reason":
            markup.insert(InlineKeyboardButton(text=f"🔘 {i[0]} {i[1]}",callback_data=vote_cb.new(name="student_",province="attend",city=i[2],school=callback_query["school"],tur=callback_query["city"],clas=callback_query["clas"],action="admin")))
        else:
            markup.insert(InlineKeyboardButton(text=f"{i[0]} {i[1]}",callback_data=vote_cb.new(name="student",province="attend",city=i[2],school=callback_query["school"],tur=callback_query["city"],clas=callback_query["clas"],action="admin")))
    markup.add(InlineKeyboardButton(text="✅ Tugatish",callback_data=vote_cb.new(name="finish",province="attend",city=callback_query["city"],school=callback_query["school"],tur="",clas=callback_query["clas"],action="admin")))
    await bot.send_message(message.from_user.id,"Kelmagan o'quvchilarni tanlang",reply_markup=markup)

async def attend_today_reason(message:types.Message,vote_cb,callback_query):
    markup = InlineKeyboardMarkup(row_width=2,reply_markup=True).row(
        InlineKeyboardButton(text="🔘 Sababli",callback_data=vote_cb.new(name="reason",province="attend",city=callback_query["city"],school=callback_query["school"],tur=callback_query["tur"],clas=callback_query["clas"],action="admin")),
        InlineKeyboardButton(text="🔴 Sababsiz",callback_data=vote_cb.new(name="no reason",province="attend",city=callback_query["city"],school=callback_query["school"],tur=callback_query["tur"],clas=callback_query["clas"],action="admin")),
    )
    await bot.send_message(message.from_user.id,"Sabablikmi yoki sababsizmi?",reply_markup=markup)

async def attend_today_student(message:types.Message,student_conn,attend_conn,vote_cb,callback_query):
    date = datetime.datetime.now().strftime("%x").split("/"); school_id = date[0]+"/"+date[2]; date = date[0]+"/"+date[2]+"/"+date[1]
    attend_conn.execute("insert into STUDENT(id,date,name,school) values (?,?,?,?);",(callback_query["city"],date,callback_query["name"],1))
    callback_query["city"] = callback_query["tur"]
    await attend_today_arr(message, student_conn, attend_conn, vote_cb, callback_query)
    if callback_query["name"] == "reason":
        print(school_id)
        reason = attend_conn.execute("select for_reason, leave from SCHOOL where id = (?) and date = (?);",(callback_query["school"],school_id)).fetchall()[0]
        if reason[0] is None:
            for_reason = 1
        else:
            for_reason = reason[0]+1
        if reason[1] is None:
            leave = 1
        else:
            leave = reason[1]+1
        attend_conn.execute("update SCHOOL set for_reason = (?), leave = (?) where id = (?) and date = (?);",(for_reason,leave,callback_query["school"],school_id))

    else:
        reason = attend_conn.execute("select for_no_reason, leave from SCHOOL where id = (?) and date = (?);",(callback_query["school"],school_id)).fetchall()[0]
        if reason[0] is None:
            for_no_reason = 1
        else:
            for_no_reason = reason[0]+1
        if reason[1] is None:
            leave = 1
        else:
            leave = reason[1]+1
        attend_conn.execute("update SCHOOL set for_no_reason = (?), leave = (?) where id = (?) and date = (?);",(for_no_reason,leave,callback_query["school"],school_id))


async def attend_today_student_(message:types.Message,student_conn,attend_conn,vote_cb,callback_query):
    date = datetime.datetime.now().strftime("%x").split("/"); school_date = date[0]+"/"+date[2]; date = date[0]+"/"+date[2]+"/"+date[1]
    student = attend_conn.execute("select name from STUDENT where id = (?) and date = (?);",(callback_query["city"],date)).fetchall()[0][0]
    attend_conn.execute("delete from STUDENT where id = (?) and date = (?);",(callback_query["city"],date))
    callback_query["city"] = callback_query["tur"]
    await attend_today_arr(message, student_conn, attend_conn, vote_cb, callback_query)
    if student == "reason":
        reason = attend_conn.execute("select for_reason, leave from SCHOOL where id = (?) and date = (?);",(callback_query["school"],school_date)).fetchall()[0]
        if reason[0]-1 <= 0:
            for_reason = None
        else:
            for_reason = reason[0]-1
        if reason[1]-1 <= 0:
            leave = None
        else:
            leave = reason[1]-1
        attend_conn.execute("update SCHOOL set for_reason = (?), leave = (?) where id = (?) and date = (?);",(for_reason,leave,callback_query["school"],school_date))

    else:
        reason = attend_conn.execute("select for_no_reason, leave from SCHOOL where id = (?) and date = (?);",(callback_query["school"],school_date)).fetchall()[0]
        if reason[0]-1 <= 0:
            for_reason = None
        else:
            for_reason = reason[0]-1
        if reason[1]-1 <= 0:
            leave = None
        else:
            leave = reason[1]-1
        attend_conn.execute("update SCHOOL set for_no_reason = (?), leave = (?) where id = (?) and date = (?);",(for_reason,leave,callback_query["school"],school_date))



async def attend_today_finish(message:types.Message,class_conn,attend_conn,admin_conn,vote_cb,callback_query):
    date = datetime.datetime.now().strftime("%x").split("/"); date = date[0]+"/"+date[2]+"/"+date[1]
    class_conn.execute("update NAME set date = (?) where number = (?);",(date,callback_query["city"]))
    classes = class_conn.execute("select date from NAME where id = (?);",(callback_query["clas"],)).fetchall()
    son = 0
    for i in classes:
        if i[0] != date:
            son = 1
    if son == 0: class_conn.execute("update NUMBER set date = (?) where number = (?);",(date,callback_query["clas"]))
    await attend_today_number(message,admin_conn,attend_conn,class_conn,vote_cb)