from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



async def governor_district_menu(message:types.Message,vote_cb):
    markup = InlineKeyboardMarkup(reply_markup=True)
    markup.row_width = 2
    markup.row(
        InlineKeyboardButton(text="+",callback_data=vote_cb.new(name="+",province="district",city="",school="",tur="None",clas="None",action="governor")),
        InlineKeyboardButton(text="-",callback_data=vote_cb.new(name="-",province="district",city="",school="",tur="None",clas="None",action="governor")),
        InlineKeyboardButton(text="🗂 Ko'rish",callback_data=vote_cb.new(name="see",province="district",city="",school="",tur="None",clas="None",action="governor"))
    )
    await bot.send_message(message.from_user.id,"Tuman qo'shmoqchimisiz yoki o'chirmoqchimisiz\nYoki shunchaki ko'rmoqchimisiz",reply_markup=markup)