from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import ReplyKeyboardRemove

from .eng import get_message_eng
from .rus import get_message_rus
from ..main_menu import main_menu
from .uzb import get_message_uzb
from ..basket.basket_uz import get_basket

from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def get_start(message: types.Message, conn):
    if message.text == "🇺🇿 O'zbekcha":
        await main_menu.get_menu_client(message, conn, "uzb")
    elif message.text == "🇷🇺 Pусский":
        await main_menu.get_menu_client(message, conn, "rus")
    elif message.text == "🇬🇧 English":
        await main_menu.get_menu_client(message, conn, "eng")


async def get_message_client(message: types.Message, conn, vote_cb):
    person = conn.execute("select language, basket, name from CLIENT where id = (?);",
                          (message.from_user.id,)).fetchall()
    person = list(person[0])
    if message.text == "📥 Savat":
        if person[1] is not None:
            await get_basket(message, conn, vote_cb)
        else:
            await bot.send_message(message.from_user.id, "Hali savat to'lmadi")
    elif message.text == "✅ Savatni to’ldirdim":
        if person[1] is not None:
            if person[2] is not None:
                await get_basket(message, conn, vote_cb)
            else:
                await bot.send_message(message.from_user.id, "Keling avval tanishib olamiz. ☺",
                                       reply_markup=ReplyKeyboardRemove())
                conn.execute("update CLIENT set bosqich = (?) where id = (?);", (10, message.from_user.id))
        elif person[1] is None:
            await bot.send_message(message.from_user.id, "Hali savatni to'ldirmadingiz!")

    elif message.text == "📥 Корзина":
        if person[1] is not None:
            await get_basket(message, conn, vote_cb)
        else:
            await bot.send_message(message.from_user.id, "Корзина еще не полная!")
    elif message.text == "✅ я наполнил корзину":
        if person[1] is not None:
            if person[2] is not None:
                await get_basket(message, conn, vote_cb)
            else:
                await bot.send_message(message.from_user.id, "Давайте сначала познакомимся. ☺",
                                       reply_markup=ReplyKeyboardRemove())
                conn.execute("update CLIENT set bosqich = (?) where id = (?);", (10, message.from_user.id))
        elif person[1] is None:
            await bot.send_message(message.from_user.id, "Вы еще не наполнили корзину!")

    elif message.text == "📥 Basket":
        if person[1] is not None:
            await get_basket(message, conn, vote_cb)
        else:
            await bot.send_message(message.from_user.id, "The basket is not full yet")
    elif message.text == "✅ I filled the basket":
        if person[1] is not None:
            if person[2] is not None:
                await get_basket(message, conn, vote_cb)
            else:
                await bot.send_message(message.from_user.id, "Let's get acquainted first. ☺",
                                       reply_markup=ReplyKeyboardRemove())
                conn.execute("update CLIENT set bosqich = (?) where id = (?);", (10, message.from_user.id))
        elif person[1] is None:
            await bot.send_message(message.from_user.id, "You haven't filled the basket yet!")

    if person[0] == "uzb":
        await get_message_uzb(message, conn, vote_cb)
    elif person[0] == "rus":
        await get_message_rus(message, conn, vote_cb)
    elif person[0] == "eng":
        await get_message_eng(message, conn, vote_cb)
