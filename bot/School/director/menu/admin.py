from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



async def director_admin_menu(message:types.Message,vote_cb):
    markup = InlineKeyboardMarkup(reply_markup=True)
    markup.row(
        InlineKeyboardButton(text="+",callback_data=vote_cb.new(name="+",province="admin",city="",school="",tur="None",clas="None",action="director")),
        InlineKeyboardButton(text="-",callback_data=vote_cb.new(name="-",province="admin",city="",school="",tur="None",clas="None",action="director")),
        InlineKeyboardButton(text="🗂 Ko'rish",callback_data=vote_cb.new(name="see",province="admin",city="",school="",tur="None",clas="None",action="director")),
    )
    await bot.send_message(message.from_user.id,"Admin qo'shmoqchimisiz yoki o'chirmoqchimisiz",reply_markup=markup)