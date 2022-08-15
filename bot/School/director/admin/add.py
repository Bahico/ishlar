from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


from config import TOKEN

# some code
from director.menu.menu import director_main_menu

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



async def director_admin_login(message:types.Message,conn,vote_cb):
    markup = InlineKeyboardMarkup(reply_markup=True).add(
        InlineKeyboardButton(text="❌STOP",callback_data=vote_cb.new(name="stop",province="stop",city="",school="",tur="None",clas="None",action="director"))
    )
    await bot.send_message(message.from_user.id,"Yangi adminning loginini kiriting",reply_markup=markup)
    conn.execute("update SAVE set text = 'add admin login' where id = (?);",(message.from_user.id,))


async def director_admin_code(message:types.Message,director_conn,conn,vote_cb):
    try: await bot.delete_message(message.from_user.id,message.message_id-1)
    except:pass
    markup = InlineKeyboardMarkup(reply_markup=True).add(
        InlineKeyboardButton(text="❌STOP",callback_data=vote_cb.new(name="stop",province="stop",city="",school="",tur="None",clas="None",action="director"))
    )
    director_conn.execute(f"update SAVE set name_text = '{message.text}' where id = (?);",(message.from_user.id,))
    await message.answer("Yangi admin kodini kiriting",reply_markup=markup)
    conn.execute("update SAVE set text = 'add admin code' where id = (?);",(message.from_user.id,))


async def director_admin_insert(message:types.Message,director_conn,admin_conn,conn,vote_cb):
    try: await bot.delete_message(message.from_user.id,message.message_id-1)
    except:pass
    login = director_conn.execute("select name_text from SAVE where id = (?);",(message.from_user.id,)).fetchall()[0][0]
    school = director_conn.execute("select name from USER where id = (?);",(message.from_user.id,)).fetchall()[0][0]
    admin_conn.execute(f"insert into CONN(id,login,code) values ({school},'{login}','{message.text}');")
    conn.execute("update SAVE set text = NULL where id = (?);",(message.from_user.id,))
    await message.answer("Qabul qilindi✅")
    await director_main_menu(message, conn, vote_cb)
