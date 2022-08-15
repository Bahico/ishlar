from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

# some code
from teacher.fan.fan import teacher_fan_new

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



async def teacher_menu_fan(message:types.Message,teacher_conn,conn,vote_cb):
    fans = teacher_conn.execute("select name from FAN where id = (?);",(message.from_user.id,)).fetchall()
    markup = InlineKeyboardMarkup(row_width=2).add(
        InlineKeyboardButton(text="Yangi",callback_data=vote_cb.new(name="new",province="fan",city="",school="",tur="None",clas="None",action="teacher"))
    )
    awa = ""
    son = 0
    for i in fans:
        fan = teacher_conn.execute("select name from FAN_CONN where number = (?);",(i[0],)).fetchall()
        if fan:
            son += 1
            awa += str(son)+". "+fan[0][0]+"\n"

    if not fans:
        await teacher_fan_new(message, teacher_conn, vote_cb)
    else:
        await bot.send_message(message.from_user.id,awa,reply_markup=markup)