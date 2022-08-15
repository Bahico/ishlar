from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from admin.menu.menu import admin_main_menu
from config import TOKEN

#some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)




async def admin_teacher_number(message:types.Message,admin_conn,class_conn,vote_cb):
    admin = admin_conn.execute("select name from USER where id = (?);",(message.from_user.id,)).fetchall()[0][0]
    arr = class_conn.execute("select name, number from NUMBER where id = (?);",(admin,)).fetchall()
    markup = InlineKeyboardMarkup(row_width=3,inline_keyboard=True)
    for i in sorted(arr):
        markup.insert(InlineKeyboardButton(text=i[0],callback_data=vote_cb.new(name="class number",province="add teacher",city=i[1],school="",tur="None",clas="None",action="admin")))
    markup.add(InlineKeyboardButton(text="⬅️ORTGA",callback_data=vote_cb.new(name="teacher",province="main menu",city="",school="",tur="None",clas="None",action="admin")))
    await bot.send_message(message.from_user.id,"Nechinchi sinfni o'qituvchisi?",reply_markup=markup)

async def admin_teacher_name(message:types.Message,class_conn,vote_cb,callback_query):
    arr = class_conn.execute("select name, number from NAME where id = (?);",(callback_query["city"],)).fetchall()
    markup = InlineKeyboardMarkup(reply_markup=True)
    markup.row_width = 2
    for i in arr:
        markup.insert(InlineKeyboardButton(text=i[0],callback_data=vote_cb.new(name="class name",province="add teacher",city=i[1],school="",tur="None",clas="None",action="admin")))
    markup.insert(InlineKeyboardButton(text="⬅️ORTGA",callback_data=vote_cb.new(name="class",province="teacher",city="",school="",tur="None",clas="None",action="admin")))
    await bot.send_message(message.from_user.id,"Qaysi sinf o'qituvchisi",reply_markup=markup)


async def admin_teacher_fan(message:types.Message,admin_conn,teacher_conn,vote_cb,callback_query):
    markup = InlineKeyboardMarkup(row_width=2)
    if callback_query["city"] != "":
        admin_conn.execute("update SAVE set name = (?) where id = (?);",(callback_query["city"],message.from_user.id))
    else:
        admin_conn.execute("update SAVE set name = NULL where id = (?);",(message.from_user.id,))
    fans = teacher_conn.execute("select name, number from FAN_CONN;").fetchall()
    for i in fans:
        markup.insert(InlineKeyboardButton(text=i[0],callback_data=vote_cb.new(name="add fan",province="add teacher",city=i[1],school="",tur="None",clas="None",action="admin")))
    markup.row(
        InlineKeyboardButton(text="Yangi",callback_data=vote_cb.new(name="new fan",province="add teacher",city="",school="",tur="None",clas="None",action="admin")),
        InlineKeyboardButton(text="❌ STOP",callback_data=vote_cb.new(name="stop",province="stop",city="",school="",tur="None",clas="None",action="admin")),
    )
    await bot.send_message(message.from_user.id,"Yangi o'qituvchini fanini tanlang",reply_markup=markup)

async def admin_teacher_fan_start(message:types.Message,conn):
    conn.execute("update SAVE set text = 'add teacher fan' where id = (?);",(message.from_user.id,))
    await bot.send_message(message.from_user.id,"Yangi fanni kiriting")

async def admin_teacher_fan_insert(message:types.Message,admin_conn,teacher_conn,conn,vote_cb):
    try: await bot.delete_message(message.from_user.id,message.message_id-1)
    except: pass
    fan = teacher_conn.execute("select number from FAN_CONN where name = (?);",(message.text,)).fetchall()
    if not fan:
        teacher_conn.execute("insert into FAN_CONN(name) values (?);",(message.text,))
        fan = teacher_conn.execute("select number from FAN_CONN where name = (?);",(message.text,)).fetchall()
    admin_conn.execute(f"update SAVE set name_text = (?) where id = (?);",(str(fan[0][0]),message.from_user.id))
    conn.execute("update SAVE set text = 'add teacher code' where id = (?);",(message.from_user.id,))
    markup = InlineKeyboardMarkup(reply_markup=True).add(InlineKeyboardButton(text="❌STOP",callback_data=vote_cb.new(name="stop",province="stop",city="",school="",tur="None",clas="None",action="admin")))
    await message.answer("Yangi o'qituvchini kodini kiriting",reply_markup=markup)


async def admin_teacher_code(message:types.Message,admin_conn,conn,vote_cb,callback_query):
    try: await bot.delete_message(message.from_user.id,message.message_id-1)
    except: pass
    conn.execute("update SAVE set text = 'add teacher code' where id = (?);",(message.from_user.id,))
    markup = InlineKeyboardMarkup(reply_markup=True).add(
        InlineKeyboardButton(text="❌STOP",callback_data=vote_cb.new(name="stop",province="stop",city="",school="",tur="None",clas="None",action="admin"))
    )
    await message.answer("Yangi o'qituvchini kodini kiriting",reply_markup=markup)
    admin_conn.execute(f"update SAVE set name_text = (?) where id = (?);",(str(callback_query["city"]),message.from_user.id))

async def admin_teacher_first(message:types.Message,admin_conn,teacher_conn,conn,vote_cb):
    try: await bot.delete_message(message.from_user.id,message.message_id-1)
    except: pass
    markup = InlineKeyboardMarkup().add(InlineKeyboardButton(text="❌ STOP",callback_data=vote_cb.new(name="stop",province="stop",city="",school="",tur="None",clas="None",action="admin")))
    await message.answer("Qabul qilindi\n\ncode:"+message.text)
    school = admin_conn.execute("select name from USER where id = (?);",(message.from_user.id,)).fetchall()[0][0]
    number = admin_conn.execute("select name, name_text from SAVE where id = (?);",(message.from_user.id,)).fetchall()[0]
    if number[0] is None:
        teacher_conn.execute(f"insert into CONN(id,fan,code) values (?,?,?)",(school,int(number[1]),message.text))
        number = teacher_conn.execute(f"select number from CONN where id = (?) and fan = (?) and code = (?);",(school,number[1],message.text)).fetchall()[0][0]
    else:
        teacher_conn.execute("insert into CONN(id,fan,class_id,code) values (?,?,?,?)",(school,int(number[1]),number[0],message.text))
        number = teacher_conn.execute("select number from CONN where id = (?) and fan = (?) and class_id = (?) and code = (?);",(school,number[1],number[0],message.text)).fetchall()[0][0]
    admin_conn.execute(f"update SAVE set name = {number}, name_text = NULL where id = (?);",(message.from_user.id,))
    conn.execute("update SAVE set text = 'add teacher first' where id = (?);",(message.from_user.id,))
    await message.answer("Yangi o'qituvchini ismini kiritng",reply_markup=markup)

async def admin_teacher_last(message:types.Message,admin_conn,conn,vote_cb):
    try: await bot.delete_message(message.from_user.id,message.message_id-1)
    except: pass
    admin_conn.execute(f"update SAVE set name_text = '{message.text}' where id = (?);",(message.from_user.id,))
    conn.execute("update SAVE set text = 'add teacher last' where id = (?);",(message.from_user.id,))
    markup = InlineKeyboardMarkup(reply_markup=True).add(
        InlineKeyboardButton(text="❌STOP",callback_data=vote_cb.new(name="stop",province="stop",city="",school="",tur="None",clas="None",action="admin"))
    )
    await message.answer("Yangi o'qituvchini familiyasini kiriting",reply_markup=markup)

async def admin_teacher_insert(message:types.Message,admin_conn,teacher_conn,conn,vote_cb):
    try: await bot.delete_message(message.from_user.id,message.message_id-1)
    except: pass
    admin = admin_conn.execute("select name, name_text from SAVE where id = (?);",(message.from_user.id,)).fetchall()[0]
    teacher_conn.execute(f"insert into name(name,last_name,first_name) values (?,?,?);",(admin[0],message.text,admin[1]))
    await message.answer(f"Qabul qilindi\n\nIsmi:{admin[1]}\nFamiliyasi:{message.text}")
    await admin_main_menu(message, conn, vote_cb)