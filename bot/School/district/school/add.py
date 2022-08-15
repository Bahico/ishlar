from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

# some code
from district.menu.menu import district_main_menu

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



async def district_school_number(message:types.Message,conn,vote_cb):
    markup = InlineKeyboardMarkup(reply_markup=True).add(
        InlineKeyboardButton(text="❌STOP",callback_data=vote_cb.new(name="stop",province="stop",city="",school="",tur="None",clas="None",action="district"))
    )
    await bot.send_message(message.from_user.id,"Yangi maktabning sonini kiriting",reply_markup=markup)
    conn.execute("update SAVE set text = 'add school number' where id = (?);",(message.from_user.id,))


async def district_school_code(message:types.Message,conn,district_conn,vote_cb):
    try:await bot.delete_message(message.from_user.id,message.message_id-1)
    except: pass
    markup = InlineKeyboardMarkup(reply_markup=True).add(
        InlineKeyboardButton(text="❌STOP",callback_data=vote_cb.new(name="stop",province="stop",city="",school="",tur="None",clas="None",action="district"))
    )
    await bot.send_message(message.from_user.id,"Yangi maktab kodini kiriting",reply_markup=markup)
    conn.execute("update SAVE set text = 'add school code' where id = (?);",(message.from_user.id,))
    district_conn.execute("update SAVE set name = (?) where id = (?);",(int(message.text),message.from_user.id))


async def district_school_insert(message:types.Message,conn,district_conn,director_conn,vote_cb):
    try:await bot.delete_message(message.from_user.id,message.message_id-1)
    except: pass
    name = district_conn.execute("select name from SAVE where id = (?);",(message.from_user.id,)).fetchall()[0][0]
    district = district_conn.execute("select name from USER where id = (?);",(message.from_user.id,)).fetchall()[0][0]
    director_conn.execute(f"insert into CONN(id,name,code) values (?,?,'{message.text}');",(district,name))
    await bot.send_message(message.from_user.id,"Qabul qilindi")
    await district_main_menu(message, conn, vote_cb)
    conn.execute("update SAVE set text = Null where id = (?);",(message.from_user.id,))
