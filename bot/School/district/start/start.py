from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

from config import TOKEN

# some code
from district.menu.menu import district_main_menu

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



async def district_province(message:types.Message,district_conn,governor_conn,family_conn,conn,vote_cb):
    district = district_conn.execute("select * from USER where id = (?);",(message.from_user.id,)).fetchall()
    if not district:
        governor = governor_conn.execute("select name, number from CONN;").fetchall()
        markup = InlineKeyboardMarkup(reply_markup=True)
        markup.row_width = 2
        for i in governor:
            markup.insert(InlineKeyboardButton(text=i[0],callback_data=vote_cb.new(name="governor",province="start",city=i[1],school="None",tur="None",clas="None",action="district")))
        await bot.send_message(message.from_user.id,"Qaysi viloyat",reply_markup=markup)
    else:
        await district_main_menu(message, conn, vote_cb)


async def district_city(message:types.Message,district_conn,vote_cb,callback_query):
    district = district_conn.execute("select name, number from CONN where id = (?);",(callback_query["city"],)).fetchall()
    markup = InlineKeyboardMarkup(reply_markup=True)
    markup.row_width = 2
    for i in district:
        markup.insert(InlineKeyboardButton(text=i[0],callback_data=vote_cb.new(name="city",province="start",city=i[1],school="",tur="None",clas="None",action="district")))
    await bot.send_message(message.from_user.id,"Qaysi tuman",reply_markup=markup)


async def district_code(message:types.Message,family_conn,conn,callback_query):
    family_conn.execute("insert into SAVE(id,name,test) values (?,?,3);",(message.from_user.id,callback_query["city"]))
    conn.execute("insert into SAVE(id,name,text) values (?,'family','district');",(message.from_user.id,))
    await bot.send_message(message.from_user.id,"Kodingizni kiriting.")


async def district_insert(message:types.Message,conn,family_conn,district_conn):
    try: await bot.delete_message(message.from_user.id,message.message_id-1)
    except: pass
    district_ = family_conn.execute("select name, test from SAVE where id = (?);",(message.from_user.id,)).fetchall()[0]
    test = district_[1]
    district = district_conn.execute("select code from CONN where number = (?);",(district_[0],)).fetchall()[0][0]
    if test > 0:
        if message.text == district:
            await message.answer("Qabul qilindi")
            family_conn.execute("delete from SAVE where id = (?);",(message.from_user.id,))
            district_conn.execute("insert into USER(name,id) values (?,?);",(district_[0],message.from_user.id))
            district_conn.execute("insert into SAVE(id) values (?);",(message.from_user.id,))
            conn.execute("update SAVE set name = 'district', text = 'contact' where id = (?);",(message.from_user.id,))
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