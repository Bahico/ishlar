from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



async def district_main_menu(message:types.Message,conn,vote_cb):
    markup = InlineKeyboardMarkup(reply_markup=True)
    markup.row_width = 2
    markup.row(
        InlineKeyboardButton(text="π«Maktablar",callback_data=vote_cb.new(name="school",province="main menu",city="",school="",tur="None",clas="None",action="district")),
        InlineKeyboardButton(text="π§Ύ Davomat",callback_data=vote_cb.new(name="attend",province="main menu",city="",school="",tur="None",clas="None",action="district")),
    )
    markup.row(
        InlineKeyboardButton(text="π Reyting",callback_data=vote_cb.new(name="rating",province="main menu",city="",school="",tur="None",clas="None",action="district")),
        InlineKeyboardButton(text="π§π»βπ« Ustozlar",callback_data=vote_cb.new(name="teachers",province="main menu",city="",school="",tur="None",clas="None",action="district")),
    )
    markup.add(
        InlineKeyboardButton(text="π§πΌβπ O'quvchilar",callback_data=vote_cb.new(name="students",province="main menu",city="",school="",tur="None",clas="None",action="district"))
    )
    await bot.send_message(message.from_user.id,"Bosh menuππ»ππ»",reply_markup=markup)
    conn.execute("update SAVE set text = NULL where id = (?);",(message.from_user.id,))