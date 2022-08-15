from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

# some code
from teacher.menu.menu import teacher_main_menu

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



async def teacher_fan_new(message:types.Message,teacher_conn,vote_cb):
    fans = teacher_conn.execute("select name, number from FAN_CONN;").fetchall()
    markup = InlineKeyboardMarkup(row_width=2)
    for i in fans:
        markup.insert(InlineKeyboardButton(text=i[0],callback_data=vote_cb.new(name="add",province="fan",city=i[1],school="",tur="None",clas="None",action="teacher")))
    markup.add(InlineKeyboardButton(text="Yangi",callback_data=vote_cb.new(name="new add",province="fan",city="",school="",tur="None",clas="None",action="teacher")))
    await bot.send_message(message.from_user.id,"Qaysi fandi qo'shmoqchisiz?",reply_markup=markup)

async def teacher_fan_insert(message:types.Message,teacher_conn,conn,vote_cb,callback_query=None):
    if callback_query is not None:
        fan = teacher_conn.execute("select * from FAN where id = (?) and name = (?);",(message.from_user.id,callback_query["city"])).fetchall()
        if not fan:
            teacher_conn.execute("insert into FAN(id,name) values (?,?);",(message.from_user.id,callback_query["city"]))
            await bot.send_message(message.from_user.id,"✅ Qo'shildi")
        else:
            await bot.send_message(message.from_user.id,"❌ Siz oldin ham bu fandi qo'shgansiz")
    else:
        fan = teacher_conn.execute("select number from FAN_CONN where name = (?);",(message.text,)).fetchall()
        if fan:
            fan = teacher_conn.execute("select * from FAN where name = (?);",(fan[0][0],)).fetchal()
            if fan:
                await bot.send_message(message.from_user.id,"❌ Siz oldin ham bu fandi qo'shgansiz")
            else:
                teacher_conn.execute("insert into FAN(name,id) values (?,?);",(fan[0][0],message.from_user.id))
                await bot.send_message(message.from_user.id,"✅ Qo'shildi")
        else:
            teacher_conn.execute("insert into FAN_CONN(name) values (?);",(message.text,))
            fan = teacher_conn.execute("select number from FAN_CONN where name = (?);",(message.text,)).fetchall()[0][0]
            teacher_conn.execute("insert into FAN(name,id) values (?,?);",(fan,message.from_user.id))
            await bot.send_message(message.from_user.id,"✅ Qo'shildi")
        conn.execute("update SAVE set text = NULL where id = (?);",(message.from_user.id,))
    await teacher_main_menu(message,conn,vote_cb)

async def teacher_fan_new_add(message:types.Message,conn,vote_cb):
    markup = InlineKeyboardMarkup().add(InlineKeyboardButton(text="❌STOP",callback_data=vote_cb.new(name="stop",province="stop",city="",school="",tur="None",clas="None",action="teacher")))
    conn.execute("update SAVE set text = 'add fan' where id = (?);",(message.from_user.id,))
    await bot.send_message(message.from_user.id,"Yangi fandi nomini kiriting",reply_markup=markup)