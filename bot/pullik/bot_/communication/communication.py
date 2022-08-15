from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

communication = None


async def get_communication(message: types.Message, conn, id, vote_cb):
    global communication
    communication = id
    markup = InlineKeyboardMarkup(resize_keyboard=True).add(InlineKeyboardButton(text="Tugatish✅",
                                                                                 callback_data=vote_cb.new(
                                                                                     location="communication",
                                                                                     text="finish", branch="None",
                                                                                     language="uzb", action="bot_")))
    await bot.send_message(message.from_user.id, "Yozishingiz mumkin. 😊", reply_markup=markup)


async def get_communication_finish(message: types.Message):
    global communication
    communication = None
    await bot.send_message(message.from_user.id,"Muloqot uchun rahmat. 😊")
