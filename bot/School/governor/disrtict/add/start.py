from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import TOKEN

# some code
from governor.menu.main_menu import governor_main_menu

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



async def governor_district_name(message:types.Message,conn,vote_cb):
    markup = InlineKeyboardMarkup(reply_markup=True).add(
        InlineKeyboardButton(text="❌STOP",callback_data=vote_cb.new(name="stop",province="stop",city="",school="",tur="None",clas="None",action="governor"))
    )
    conn.execute("update SAVE set text = 'add district name' where id = (?);",(message.from_user.id,))
    await bot.send_message(message.from_user.id,"Yangi tuman nomini kiriting",reply_markup=markup)


async def governor_district_code(message:types.Message,conn,governor_conn):
    try:await bot.delete_message(message.from_user.id,message.message_id-1)
    except: pass
    conn.execute("update SAVE set text = 'add district code' where id = (?);",(message.from_user.id,))
    governor_conn.execute(f"update SAVE set name_text = (?) where id = (?);",(message.text,message.from_user.id,))
    await message.answer("Yangi tuman kodini kiriting")


async def governor_district_insert(message:types.Message,conn,governor_conn,district_conn,vote_cb):
    try:await bot.delete_message(message.from_user.id,message.message_id-1)
    except: pass
    conn.execute("update SAVE set text = NULL where id = (?);",(message.from_user.id,))
    name = governor_conn.execute("select name_text from SAVE where id = (?);",(message.from_user.id,)).fetchall()[0]
    school = governor_conn.execute("select name from USER where id = (?);",(message.from_user.id,)).fetchall()[0]
    district_conn.execute(f"insert into CONN(id,name,code) values (?,(?),(?));",(school[0],name[0],message.text))
    await message.answer(f"Qabul qilindi✅\nTuman nomi:{name[0]}\ncode:{message.text}")
    await governor_main_menu(message, conn, vote_cb)