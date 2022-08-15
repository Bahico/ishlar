from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

#some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



async def admin_teacher_menu(message:types.Message,vote_cb):
    markup = InlineKeyboardMarkup(reply_markup=True)
    markup.row_width = 2
    markup.row(
        InlineKeyboardButton(text="+",callback_data=vote_cb.new(name="+",province="teacher",city="",school="",tur="None",clas="None",action="admin")),
        InlineKeyboardButton(text="-",callback_data=vote_cb.new(name="-",province="teacher",city="",school="",tur="None",clas="None",action="admin")),
        InlineKeyboardButton(text="🗂 Ko'rish",callback_data=vote_cb.new(name="see",province="teacher",city="",school="",tur="None",clas="None",action="admin")),
    )
    await bot.send_message(message.from_user.id,"O'qituvchi qo'shasizmi yoki o'chirasizmi\n\nIltimos sinflarni qo'shib bolgach o'qituvchilarni qo'shing",reply_markup=markup)


async def admin_teacher_class(message:types.Message,vote_cb):
    markup = InlineKeyboardMarkup(reply_markup=True).row(
        InlineKeyboardButton(text="Sinf ham",callback_data=vote_cb.new(name="class",province="teacher",city="",school="",tur="None",clas="None",action="admin")),
        InlineKeyboardButton(text="Faqat fan",callback_data=vote_cb.new(name="fan",province="teacher",city="",school="",tur="None",clas="None",action="admin")),
    )
    await bot.send_message(message.from_user.id,"Yangi o'qituvchini faqat fandan dars otadimi yoki sinf ham bormi?",reply_markup=markup)
