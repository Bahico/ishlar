from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

#some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



async def admin_class(message:types.Message,vote_cb):
    markup = InlineKeyboardMarkup(reply_markup=True)
    markup.row(
        InlineKeyboardButton(text="+",callback_data=vote_cb.new(name="+",province="class",city="None",school="None",tur="None",clas="None",action="admin")),
        InlineKeyboardButton(text="-",callback_data=vote_cb.new(name="-",province="class",city="None",school="None",tur="None",clas="None",action="admin")),
        InlineKeyboardButton(text="🗂 Ko'rish",callback_data=vote_cb.new(name="see",province="menu",city="None",school="None",tur="None",clas="None",action="admin"))
    )
    await bot.send_message(message.from_user.id,"Sinf qo'shmoqchimisiz yoki o'chirmoqchimisiz",reply_markup=markup)