from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



async def director_attend_menu(message:types.Message,vote_cb):
    markup = InlineKeyboardMarkup(row_width=2,reply_markup=True).row(
        InlineKeyboardButton(text="Maktabni",callback_data=vote_cb.new(name="type tur",province="attend",city="school",school="",tur="None",clas="None",action="director")),
        InlineKeyboardButton(text="O'quvchilarni",callback_data=vote_cb.new(name="type tur",province="attend",city="student",school="",tur="None",clas="None",action="director"))
    )
    await bot.send_message(message.from_user.id,"Maktabni davomatini tekshirmoqchimisiz yoki o'quvchilarni",reply_markup=markup)


async def director_attend_lifetime(message:types.Message,vote_cb,callback_query):
    markup = InlineKeyboardMarkup(reply_markup=True).row(
        InlineKeyboardButton(text="Yillik",callback_data=vote_cb.new(name="type lifetime",province="attend",city="",school="",tur="year",clas=callback_query["city"],action="director")),
        InlineKeyboardButton(text="Oylik",callback_data=vote_cb.new(name="type lifetime",province="attend",city="",school="",tur="month",clas=callback_query["city"],action="director")),
        InlineKeyboardButton(text="Kunlik",callback_data=vote_cb.new(name="type lifetime",province="attend",city="",school="",tur="day",clas=callback_query["city"],action="director")),
    )
    await bot.send_message(message.from_user.id,"Davomatni qanday ko'rmoqchisiz",reply_markup=markup)