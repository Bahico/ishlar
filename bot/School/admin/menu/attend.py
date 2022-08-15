from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

#some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def admin_attend_menu(message:types.Message,vote_cb):
    markup = InlineKeyboardMarkup(row_width=2).row(
        InlineKeyboardButton(text="Yangi kun",callback_data=vote_cb.new(name="today",province="attend",city="None",school="None",tur="None",clas="None",action="admin")),
        InlineKeyboardButton(text="Tekshiruv",callback_data=vote_cb.new(name="inspection",province="attend",city="None",school="None",tur="None",clas="None",action="admin"))
    )
    await bot.send_message(message.from_user.id,"Menudan kerakligini tanlang",reply_markup=markup)