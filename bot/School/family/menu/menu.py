from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



async def family_main_menu(message:types.Message,conn,vote_cb):
    markup = InlineKeyboardMarkup(reply_markup=True)
    markup.row_width = 2
    markup.row(
        InlineKeyboardButton(text="🧑🏻‍🎓Bolalarim",callback_data=vote_cb.new(name="student",province="main menu",city="None",school="None",tur="None",clas="None",action="admin")),
        InlineKeyboardButton(text="🧑🏻‍🏫Ustozlar",callback_data=vote_cb.new(name="teacher",province="main menu",city="None",school="None",tur="None",clas="None",action="admin")),
        InlineKeyboardButton(text="📆Davomat",callback_data=vote_cb.new(name="today",province="main menu",city="None",school="None",tur="None",clas="None",action="admin")),
        InlineKeyboardButton(text="📊Reyting",callback_data=vote_cb.new(name="rating",province="main menu",city="None",school="None",tur="None",clas="None",action="admin"))
    )
    await bot.send_message(message.from_user.id,"Bosh menu",reply_markup=markup)
    conn.execute("update SAVE set text = NULL where id = (?);",(message.from_user.id,))