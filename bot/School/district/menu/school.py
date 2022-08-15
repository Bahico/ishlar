from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



async def district_school_menu(message:types.Message,vote_cb):
    markup = InlineKeyboardMarkup(reply_markup=True)
    markup.row_width = 2
    markup.row(
        InlineKeyboardButton(text="+",callback_data=vote_cb.new(name="+",province="school",city="",school="",tur="None",clas="None",action="district")),
        InlineKeyboardButton(text="-",callback_data=vote_cb.new(name="-",province="school",city="",school="",tur="None",clas="None",action="district")),
        InlineKeyboardButton(text="🗂 Ko'rish",callback_data=vote_cb.new(name="see",province="school",city="",school="",tur="None",clas="None",action="district"))
    )
    await bot.send_message(message.from_user.id,"Maktab qo'shmoqchimisiz yoki o'chirmoqchimisiz",reply_markup=markup)
