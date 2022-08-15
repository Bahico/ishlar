from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

from config import TOKEN

# some code
from teacher.menu.menu import teacher_main_menu

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



async def teacher_province(message:types.Message,teacher_conn,governor_conn,conn,vote_cb):
    teacher = teacher_conn.execute("select * from USER where id = (?);",(message.from_user.id,)).fetchall()
    if not teacher:
        markup = InlineKeyboardMarkup(row_width=2,reply_markup=True)
        governor = governor_conn.execute("select name, number from CONN;")
        for i in governor:
            markup.insert(InlineKeyboardButton(text=i[0],callback_data=vote_cb.new(name="province", province="start",city=i[1], school="", tur="None",clas="None", action="teacher")))
        await bot.send_message(message.from_user.id,"Viloyatingizni tanlang",reply_markup=markup)
    else:
        await teacher_main_menu(message, conn, vote_cb)


async def teacher_city(message:types.Message,district_conn,vote_cb,callback_query):
    markup = InlineKeyboardMarkup(row_width=2,reply_markup=True)
    district = district_conn.execute("select name, number from CONN where id = (?);",(callback_query["city"],)).fetchall()
    for i in district:
         markup.insert(InlineKeyboardButton(text=i[0],callback_data=vote_cb.new(name="city", province="start",city=i[1], school="", tur="None",clas="None", action="teacher")))
    await bot.send_message(message.from_user.id,"Tumaningizni tanlang",reply_markup=markup)

async def teacher_school(message:types.Message,director_conn,vote_cb,callback_query):
    markup = InlineKeyboardMarkup(row_width=2,reply_markup=True)
    school = director_conn.execute("select name, number from CONN where id = (?);",(callback_query["city"],)).fetchall()
    for i in school:
        markup.insert(InlineKeyboardButton(text=i[0],callback_data=vote_cb.new(name="school", province="start",city=i[1], school="", tur="None",clas="None", action="teacher")))
    await bot.send_message(message.from_user.id,"Maktabingizni tanlang",reply_markup=markup)

async def teacher_fan(message:types.Message,teacher_conn,vote_cb,callback_query):
    markup = InlineKeyboardMarkup(row_width=2,reply_markup=True)
    teachers = teacher_conn.execute("select fan from CONN where id = (?);",(callback_query["city"],)).fetchall()
    teacher_set = set()
    for i in teachers:
        teacher_set.add(i[0])
    for i in teacher_set:
        fan = teacher_conn.execute("select name, number from FAN_CONN where number = (?);",(i,)).fetchall()[0]
        markup.insert(InlineKeyboardButton(text=fan[0],callback_data=vote_cb.new(name="fan", province="start",city=fan[1], school=callback_query["city"], tur="None",clas="None", action="teacher")))
    await bot.send_message(message.from_user.id,"Qaysi fandan dars otasiz?",reply_markup=markup)

async def teacher_teachers(message:types.Message,teacher_conn,vote_cb,callback_query):
    markup = InlineKeyboardMarkup(row_width=2,reply_markup=True)
    teachers = teacher_conn.execute(f"select number from CONN where id = (?) and fan = (?);",(callback_query["school"],callback_query["city"])).fetchall()
    for i in teachers:
        teacher = teacher_conn.execute("select last_name, first_name from NAME where name = (?);",(i[0],)).fetchall()[0]
        markup.insert(InlineKeyboardButton(text=f"{teacher[1]} {teacher[0]}",callback_data=vote_cb.new(name="my", province="start",city=i[0], school="", tur="None",clas="None", action="teacher")))
    await bot.send_message(message.from_user.id,"Qaysi birisiz?",reply_markup=markup)

async def teacher_teacher(message:types.Message,family_conn,conn,callback_query):
    family_conn.execute("delete from SAVE where id = (?);",(message.from_user.id,))
    family_conn.execute("insert into SAVE(id,name,test) values (?,?,3);",(message.from_user.id,callback_query["city"]))
    conn.execute("insert into SAVE(id,name,text) values (?,'family','teacher');",(message.from_user.id,))
    await bot.send_message(message.from_user.id,"Kodingizni kiriting")

async def teacher_insert(message:types.Message, family_conn, teacher_conn, conn):
    try: await bot.delete_message(message.from_user.id,message.message_id-1)
    except: pass
    teacher = family_conn.execute("select name, test from SAVE where id = (?);",(message.from_user.id,)).fetchall()[0]
    test = teacher[1]
    governor = teacher_conn.execute("select code from CONN where number = (?);",(teacher[0],)).fetchall()[0][0]
    if test > 0:
        if message.text == governor:
            await message.answer("Qabul qilindi")
            family_conn.execute("delete from SAVE where id = (?);",(message.from_user.id,))
            teacher_conn.execute("insert into USER(id,name) values (?,?);",(message.from_user.id,teacher[0]))
            conn.execute("update SAVE set name = 'teacher', text = 'contact' where id = (?);",(message.from_user.id,))
            markup = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("❌Telefon raqamim",request_contact=True))
            await message.answer("Telefon raqamingizni kiriting",reply_markup=markup)
            await bot.delete_message(message.from_user.id,message.message_id+1)
        else:
            family_conn.execute("update SAVE set test = (?) where id = (?);",(test-1,message.from_user.id))
            await message.answer(f"Iltimos togri kiriting\n\nSizda {str(test)} imkoniyati bor")
    else:
        family_conn.execute("delete from SAVE where id = (?);",(message.from_user.id,))
        conn.execute("delete from SAVE where id = (?);",(message.from_user.id,))
        await message.answer("Iltimos botda tog'ri foydalaning")