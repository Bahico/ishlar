from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

from config import TOKEN

# some code
from director.menu.menu import director_main_menu

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def director_start_province(message: types.Message, director_conn, governor_conn, conn, vote_cb):
    director = director_conn.execute("select * from USER where id = (?);",(message.from_user.id,)).fetchall()
    if not director:
        province = governor_conn.execute("select name, number from CONN;").fetchall()
        markup = InlineKeyboardMarkup(row_width=2,reply_markup=True)
        for i in province:
            markup.insert(InlineKeyboardButton(text=i[0],callback_data=vote_cb.new(name="province",province="start",city=i[1],school="",tur="None",clas="None",action="director")))
        await bot.send_message(message.from_user.id,"Qaysi viloyat",reply_markup=markup)
    else:
        await director_main_menu(message, conn, vote_cb)

async def director_start_district(message:types.Message, district_conn, vote_cb, callback_query):
    district = district_conn.execute("select name, number from CONN where id = (?);",(callback_query["city"],)).fetchall()
    markup = InlineKeyboardMarkup(reply_markup=True)
    markup.row_width = 2
    for i in district:
        markup.insert(InlineKeyboardButton(text=i[0],callback_data=vote_cb.new(name="city",province="start",city=i[1],school="",tur="None",clas="None",action="director")))
    await bot.send_message(message.from_user.id,"Qaysi tuman",reply_markup=markup)

async def director_start_school(message:types.Message, director_conn, vote_cb, callback_query):
    school = director_conn.execute("select name, number from CONN where id = (?);",(callback_query["city"],)).fetchall()
    markup = InlineKeyboardMarkup(reply_markup=True)
    markup.row_width = 3
    for i in school:
        markup.insert(InlineKeyboardButton(text=i[0],callback_data=vote_cb.new(name="school",province="start",city=i[1],school="",tur="None",clas="None",action="director")))
    await bot.send_message(message.from_user.id,"Qaysi maktab",reply_markup=markup)

async def director_start_code(message:types.Message, conn, family_conn, callback_query):
    conn.execute("insert into SAVE(id,name,text) values (?,'family','director');",(message.from_user.id,))
    family_conn.execute("insert into SAVE(id,name,test) values (?,?,3);",(message.from_user.id,callback_query["city"]))
    await bot.send_message(message.from_user.id,"Kodingizni kiriting")

async def director_start_insert(message:types.Message, conn, family_conn, director_conn):
    try: await bot.delete_message(message.from_user.id,message.message_id-1)
    except: pass
    director_  = family_conn.execute("select name, test from SAVE where id = (?);",(message.from_user.id,)).fetchall()[0]
    test = director_[1]
    governor = director_conn.execute("select code from CONN where number = (?);",(director_[0],)).fetchall()[0][0]
    if test > 0:
        if message.text == governor:
            await message.answer("Qabul qilindi")
            family_conn.execute("delete from SAVE where id = (?);",(message.from_user.id,))
            director_conn.execute("insert into USER(name,id) values (?,?);",(director_[0],message.from_user.id))
            director_conn.execute("insert into SAVE(id) values (?);",(message.from_user.id,))
            conn.execute("update SAVE set name = 'director', text = 'contact' where id = (?);",(message.from_user.id,))
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