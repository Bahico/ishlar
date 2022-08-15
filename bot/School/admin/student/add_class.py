from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

#some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



async def admin_class_number_add(message:types.Message, class_conn, conn, vote_cb):
    class_s = class_conn.execute("select name, number from NUMBER;").fetchall()
    markup = InlineKeyboardMarkup(reply_markup=True)
    markup.row_width = 3
    for i in class_s:
        markup.insert(InlineKeyboardButton(text=i[0],callback_data=vote_cb.new(name="number",province="class",city=i[1],school="None",tur="None",clas="None",action="admin")))
    markup.insert(InlineKeyboardButton(text="Yangi",callback_data=vote_cb.new(name="number",province="class",city="new",school="None",tur="None",clas="None",action="admin")))
    markup.add(InlineKeyboardButton(text="⬅️ORTGA",callback_data=vote_cb.new(name="main menu",province="menu",city="",school="None",tur="None",clas="None",action="admin")))
    if class_s: await bot.send_message(message.from_user.id,"Nechinchi sinf qo'shiladi\n\nYoki yangi sinf qo'shiladimi",reply_markup=markup)
    else: await admin_class_new_number(message,conn)


async def admin_class_new_number(message:types.Message,conn):
    conn.execute("update SAVE set text = 'add class number' where id = (?);",(message.from_user.id,))
    await bot.send_message(message.from_user.id,"Yangi sinfni kiriting")


async def admin_class_insert(message:types.Message, class_conn, conn, vote_cb, admin_conn):
    try: await bot.delete_message(message.from_user.id,message.message_id-1)
    except: pass
    admin = admin_conn.execute("select name from user where id = (?);",(message.from_user.id,)).fetchall()[0][0]
    try:
        int(message.text)
        class_conn.execute("insert into NUMBER(id,name) values (?,?);",(admin,int(message.text)))
        await admin_class_number_add(message, class_conn, conn, vote_cb)
    except:
        add = message.text
        class_conn.execute("insert into NAME(id,name) values (?,?);",(admin,add.upper()))
        await admin_class_number_add(message, class_conn, conn, vote_cb)
    conn.execute("update SAVE set text = NULL where id = (?);",(message.from_user.id,))


async def admin_class_tur(message:types.Message,conn):
    conn.execute("update SAVE set text = 'add class tur' where id = (?);",(message.from_user.id,))
    await bot.send_message(message.from_user.id,"Yangi sinfni kiriting")
