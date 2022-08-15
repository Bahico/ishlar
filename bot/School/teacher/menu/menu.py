from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



async def teacher_main_menu(message:types.Message,conn,vote_cb):
    markup = InlineKeyboardMarkup(row_width=2,reply_markup=True).row(
        InlineKeyboardButton(text="🧾 Davomat",callback_data=vote_cb.new(name="attend",province="main menu",city="",school="",tur="None",clas="None",action="teacher")),
        InlineKeyboardButton(text="Fanlar",callback_data=vote_cb.new(name="fan",province="main menu",city="",school="",tur="None",clas="None",action="teacher")),
    )
    markup.row(
        InlineKeyboardButton(text="📊 Reyting",callback_data=vote_cb.new(name="rating",province="main menu",city="",school="",tur="None",clas="None",action="teacher")),
        InlineKeyboardButton(text="Muloqot",callback_data=vote_cb.new(name="communication",province="main menu",city="",school="",tur="None",clas="None",action="teacher")),
    )
    markup.row(
        InlineKeyboardButton(text="⚙️O'z sozlamalarim",callback_data=vote_cb.new(name="my setting",province="main menu",city="",school="",tur="None",clas="None",action="teacher")),
    )
    await bot.send_message(message.from_user.id,"Bosh menu",reply_markup=markup)
    conn.execute("update SAVE set text = NULL where id = (?);",(message.from_user.id,))