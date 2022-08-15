from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from admin.menu.menu import admin_main_menu
from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def admin_login(message:types.Message,admin_conn,family_conn,conn,vote_cb):
    admin = admin_conn.execute("select * from USER where id = (?);",(message.from_user.id,)).fetchall()
    if not admin:
        family_conn.execute("insert into SAVE(id,test,name_text) values (?,?,'login');",(message.from_user.id,3))
        await bot.send_message(message.from_user.id,"Loginingizni kiriting")
        conn.execute("insert into SAVE(id,name,text) values (?,'family','admin');",(message.from_user.id,))
    else:
        await admin_main_menu(message,conn,vote_cb)

async def admin_code(message:types.Message,admin_conn,family_conn,conn):
    try: await bot.delete_message(message.from_user.id,message.message_id-1)
    except:pass

    login = family_conn.execute("select name_text, test, name from SAVE where id = (?);",(message.from_user.id,)).fetchall()[0]
    if login[0] == "login":
        admin = admin_conn.execute(f"select number from CONN where login = '{message.text}';").fetchall()
        if admin:
            family_conn.execute("update SAVE set name = (?), name_text = 'code' where id = (?);",(admin[0][0],message.from_user.id,))
            await message.answer("Kodni kiriting")
        else:
            await message.answer("Xato!\n\nerror login: "+message.text)
            family_conn.execute("delete from SAVE where id = (?);",(message.from_user.id,))
    else:
        code = admin_conn.execute("select code from CONN where number = (?);",(login[2],)).fetchall()[0]
        test = login[1]-1
        if test > 0:
            if code[0] == message.text:
                await message.answer("Qabul qilindi")
                family_conn.execute("delete from SAVE where id = (?);",(message.from_user.id,))
                admin_conn.execute("insert into USER(name,id) values (?,?);",(login[2],message.from_user.id))
                admin_conn.execute("insert into SAVE(id) values (?);",(message.from_user.id,))
                conn.execute("update SAVE set name = 'admin', text = 'contact' where id = (?);",(message.from_user.id,))
                markup = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("❌Telefon raqamim",request_contact=True))
                await message.answer("Telefon raqamingizni kiriting",reply_markup=markup)
                await bot.delete_message(message.from_user.id,message.message_id+1)
            else:
                conn.execute("update SAVE set test = (?) where id = (?);",(test,message.from_user.id))
                await message.answer("Xato!\n\nerror code: "+message.text)
        else:
            family_conn.execute("delete from SAVE where id = (?);",(message.from_user.id,))
            conn.execute("delete from SAVE where id = (?);")
            await message.answer("Iltimos botdan to'g'ri foydalaning")