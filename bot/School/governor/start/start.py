from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

from config import TOKEN

# some code
from governor.menu.main_menu import governor_main_menu

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



async def governor_governor(message:types.Message,governor_conn,family_conn,conn,vote_cb):
    try: await bot.delete_message(message.from_user.id,message.message_id-1)
    except: pass
    governor = governor_conn.execute("select * from USER where id = (?);",(message.from_user.id,)).fetchall()
    if not governor:
        family_conn.execute("delete from CONN where id = (?);",(message.from_user.id,))
        governor = governor_conn.execute("select name, number from CONN;").fetchall()
        markup = InlineKeyboardMarkup(reply_markup=True)
        markup.row_width = 2
        for i in governor:
            markup.insert(InlineKeyboardButton(text=i[0],callback_data=vote_cb.new(name="governor",province="start",city=i[1],school=i[0],tur="None",clas="None",action="governor")))
        await bot.send_message(message.from_user.id,"Qaysi tuman",reply_markup=markup)
    else:
        await governor_main_menu(message, conn, vote_cb)

# Andijon,baha,1212
async def governor_province(message:types.Message,family_conn,conn,callback_query):
    await bot.send_message(message.from_user.id,callback_query["school"]+" ning kodini kiriting")
    family_conn.execute("insert into SAVE(name,id,test) values (?,?,3);",(callback_query["city"],message.from_user.id))
    conn.execute("insert into SAVE(id,name,text) values (?,'family','governor');",(message.from_user.id,))



async def governor_code(message:types.Message,family_conn,governor_conn,conn):
    try: await bot.delete_message(message.from_user.id,message.message_id-1)
    except: pass
    governor_ = family_conn.execute("select name, test from SAVE where id = (?);",(message.from_user.id,)).fetchall()[0]
    test = governor_[1]
    governor = governor_conn.execute("select code from CONN where number = (?);",(governor_[0],)).fetchall()[0][0]
    if test > 0:
        if message.text == governor:
            await message.answer("Qabul qilindi")
            family_conn.execute("delete from SAVE where id = (?);",(message.from_user.id,))
            governor_conn.execute("insert into USER(name,id) values (?,?);",(governor_[0],message.from_user.id))
            governor_conn.execute("insert into SAVE(id) values (?);",(message.from_user.id,))
            conn.execute("update SAVE set name = 'governor', text = 'contact' where id = (?);",(message.from_user.id,))
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