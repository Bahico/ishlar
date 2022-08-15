from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from admin.menu.menu import admin_main_menu
from admin.student.add_class import admin_class_new_number
from config import TOKEN

#some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



async def admin_class_number(message:types.Message,admin_conn,class_conn,conn,vote_cb):
    school_id = admin_conn.execute("select name from USER where id = (?);",(message.from_user.id,)).fetchall()[0][0]
    school_id = admin_conn.execute("select id from CONN where number = (?);",(school_id,)).fetchall()[0][0]
    arr = class_conn.execute("select name, number from NUMBER where id = (?);",(school_id,)).fetchall()
    markup = InlineKeyboardMarkup(reply_markup=True)
    markup.row_width = 2
    for i in arr:
        markup.insert(InlineKeyboardButton(text=i[0],callback_data=vote_cb.new(name="class number",province="add student",city=i[1],school="None",tur="None",clas="None",action="admin")))
    if arr:await bot.send_message(message.from_user.id,"Nechinchi sinfga o'quvchi qo'shmoqchisiz",reply_markup=markup)
    else: await admin_class_new_number(message,conn)


async def admin_class_name(message:types.Message,class_conn,vote_cb,callback_query):
    arr = class_conn.execute("select name, number from NAME where id = (?);",(callback_query["city"],)).fetchall()
    markup = InlineKeyboardMarkup(reply_markup=True)
    markup.row_width = 2
    for i in arr:
        markup.insert(InlineKeyboardButton(text=i[0],callback_data=vote_cb.new(name="class name",province="add student",city=i[1],school="None",tur="None",clas="None",action="admin")))
    await bot.send_message(message.from_user.id,"Qaysi sinfga o'quvchi qo'shmoqchisiz",reply_markup=markup)


async def admin_student_last(message:types.Message,admin_conn,conn,vote_cb,callback_query):
    admin_conn.execute("update SAVE set name = (?) where id = (?);",(callback_query["city"],message.from_user.id))
    conn.execute("update SAVE set text = 'add student first name' where id = (?);",(message.from_user.id,))
    markup = InlineKeyboardMarkup(reply_markup=True).add(
        InlineKeyboardButton(text='❌STOP',callback_data=vote_cb.new(name="stop",province="stop",city="",school="None",tur="None",clas="None",action="admin"))
    )
    await bot.send_message(message.from_user.id,"Qo'shiladigan o'quvchini ismini kiriting",reply_markup=markup)

async def admin_student_first(message:types.Message,admin_conn,conn):
    try: await bot.delete_message(message.from_user.id,message.message_id-1)
    except: pass
    admin_conn.execute(f"update SAVE set name_text = '{message.text}' where id = (?);",(message.from_user.id,))
    conn.execute("update SAVE set text = 'add student last name' where id = (?);",(message.from_user.id,))
    await message.answer("Qo'shiladigan o'quvchini familiyasini kiriting")

async def admin_student_father(message:types.Message,admin_conn,student_conn,conn,vote_cb):
    try: await bot.delete_message(message.from_user.id,message.message_id-1)
    except: pass
    markup = InlineKeyboardMarkup(reply_markup=True).add(
        InlineKeyboardButton(text="Keynroq",callback_data=vote_cb.new(name="stop",province="stop",city="",school="None",tur="None",clas="None",action="admin"))
    )
    admin = admin_conn.execute("select name, name_text from SAVE where id = (?);",(message.from_user.id,)).fetchall()[0]
    student_conn.execute("insert into CONN(id,last_name,first_name) values (?,?,?);",(admin[0],message.text,admin[1]))
    number = student_conn.execute(f"select number from CONN where id = (?) and last_name = (?) and first_name = (?);",(admin[0],message.text,admin[1])).fetchall()[0][0]
    conn.execute("update SAVE set text = 'add student father' where id = (?);",(message.from_user.id,))
    admin_conn.execute("update SAVE set name = (?) where id = (?);",(number,message.from_user.id))
    await message.answer(f"Yangi o'quvchini otasini ismini kiriting\n\nYoki keynroq kirgizing\n\nIsmi:{admin[1]}\nFamiliyasi:{message.text}",reply_markup=markup)

async def admin_student_mother(message:types.Message,admin_conn,conn):
    try: await bot.delete_message(message.from_user.id,message.message_id-1)
    except: pass
    admin_conn.execute(f"update SAVE set name_text = '{message.text}' where id = (?);",(message.from_user.id,))
    conn.execute("update SAVE set text = 'add student mother' where id = (?);",(message.from_user.id,))
    await message.answer("Yangi o'quvchini onasini ismini kiriting")

async def admin_student_family(message:types.Message,admin_conn,student_conn,conn):
    try: await bot.delete_message(message.from_user.id,message.message_id-1)
    except: pass
    admin = admin_conn.execute("select name_text, name from SAVE where id = (?);",(message.from_user.id,)).fetchall()[0]
    student_conn.execute(f"insert into FAMILY(id,father,mather) values ({admin[1]},'{admin[0]}','{message.text}');")
    conn.execute("update SAVE set text = 'add student code' where id = (?);",(message.from_user.id,))
    await message.answer("Yangi o'quvchini codini kiriting\n\nOtasini ismi: "+admin[0]+"\nOnasini ismi: "+message.text)

async def admin_student_code(message:types.Message,admin_conn,student_conn,conn,vote_cb):
    try: await bot.delete_message(message.from_user.id,message.message_id-1)
    except: pass
    admin = admin_conn.execute("select name from SAVE where id = (?);",(message.from_user.id,)).fetchall()[0]
    student_conn.execute(f"insert into CODE(id,code) values ({admin[0]},'{message.text}');")
    conn.execute("update SAVE set text = NULL where id = (?);",(message.from_user.id,))
    admin_conn.execute("update SAVE set name_text = NULL, name = NULL where id = (?);",(message.from_user.id,))
    await message.answer("Qabul qilindi\n\ncode: "+message.text)
    await admin_main_menu(message,conn,vote_cb)