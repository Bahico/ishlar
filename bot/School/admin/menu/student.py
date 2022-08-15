from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

#some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def admin_student(message:types.Message,vote_cb):
    markup = InlineKeyboardMarkup(reply_markup=True)
    markup.row_width = 2
    markup.row(
        InlineKeyboardButton(text="+",callback_data=vote_cb.new(name="+",province="student",city="",school="",tur="None",clas="None",action="admin")),
        InlineKeyboardButton(text="-",callback_data=vote_cb.new(name="-",province="student",city="",school="",tur="None",clas="None",action="admin")),
        InlineKeyboardButton(text="🗂 Ko'rish",callback_data=vote_cb.new(name="see",province="student",city="",school="",tur="None",clas="None",action="admin")),
    )
    await bot.send_message(message.from_user.id,"O'quvchi qo'shmoqchimisiz yoki o'chirmoqchimisiz",reply_markup=markup)