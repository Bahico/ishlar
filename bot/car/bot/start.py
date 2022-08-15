from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from config import TOKEN

# some code

# "id", "language", "action"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def bot_start(message: types.Message, conn):
    """
    Botni katta admini bolish uchun start
    :param message:
    :param conn:
    :return: kod soraydi
    """
    bot_ = conn.execute("select * from I_ where id = (?);", (message.from_user.id,)).fetchall()
    if not bot_:
        await bot.send_message(message.from_user.id, "Password:")
        conn.execute("insert into I_(id,settings) values (?,'start');", (message.from_user.id,))
