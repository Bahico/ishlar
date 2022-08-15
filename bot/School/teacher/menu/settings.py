from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

# some code
from teacher.menu.menu import teacher_main_menu

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



async def teacher_settings_menu(message:types.Message,vote_cb):
    markup = InlineKeyboardMarkup(row_width=2).row(
        InlineKeyboardButton(text="Kodni o'zgartirish",callback_data=vote_cb.new(name="edit code",province="settings",city="",school="",tur="None",clas="None",action="teacher"))
    )
    await bot.send_message(message.from_user.id,"Tanlang👇🏻👇🏻",reply_markup=markup)

async def teacher_settings_edit_code(message:types.Message,conn,vote_cb):
    conn.execute("update SAVE set text = 'edit code' where id = (?);",(message.from_user.id,))
    markup = InlineKeyboardMarkup().add(
        InlineKeyboardButton(text="❌STOP",callback_data=vote_cb.new(name="stop",province="stop",city="",school="",tur="None",clas="None",action="teacher"))
    )
    await bot.send_message(message.from_user.id,"Yangi kodni kiriting",reply_markup=markup)

async def teacher_edit_code(message:types.Message,teacher_conn,conn,vote_cb):
    try: await bot.delete_message(message.from_user.id,message.message_id-1)
    except: pass
    teacher = teacher_conn.execute("select name from user where id = (?);",(message.from_user.id,)).fetchall()[0][0]
    teacher_conn.execute("update CONN set code = (?) where number = (?);",(message.text,teacher))
    conn.execute("update SAVE set text = NULL where id = (?);",(message.from_user.id,))
    await message.answer("✅Qabul qilindi")
    await teacher_main_menu(message, conn, vote_cb)