from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from ..food_settings import callback_uzb
from ..main_menu import main_menu
from ..delivery import delivery, branch
from ..food_menu import food_menu, callback_food_menu_uzb
from ..food import callback_food_uzb
from ..user.user_name import get_user_name
from ..phone_number.phone_number import get_phone
from ..history.history import get_history

from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def get_message_eng(message: types.Message, conn, vote_cb):
    person = conn.execute("select bosqich, basket, branch, tur, basket, comment from CLIENT where id = (?);",
                          (message.from_user.id,)).fetchall()
    person = list(person[0])
    if person[-1] is not None:
        if message.text != "STOP":
            await bot.send_message(person[-1], message.text)
        else:
            conn.execute("update CLIENT set comment = NULL where id = (?);", (message.from_user.id,))
            await bot.send_message(message.from_user.id, "Thanks for the chat😊")
    elif person[0] == 1:
        if message.text == "🍽 Menu":
            await delivery.get_delivery(message, conn, "eng")
        elif message.text == "📖 Order history":
            await get_history(message,conn,"eng")
        elif message.text == "✍️ Give feedback":
            conn.execute("update CLIENT set comment = (?) where id = (?);", ())
            markup = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("STOP"))
            await bot.send_message(message.from_user.id,
                                   "You can write\n\nWhen you have finished recording, press the STOP button",
                                   reply_markup=markup)
        elif message.text == "☎️ Contact us":
            await bot.send_message(message.from_user.id,
                                   "If you have any questions you can write or call us:\n📨@DwichuzAdmin   \n📞+998974109750")
    elif person[0] == 2:
        if message.text == "🏃 Take away":
            conn.execute("update CLIENT set delivery = (?), bosqich = 13 where id = (?);",
                         ("take", message.from_user.id))
            markup = ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(KeyboardButton("📱 My phone number", request_contact=True))
            markup.add(KeyboardButton("⬅️ Back"))
        elif message.text == "⬅️ Back":
            await main_menu.get_menu_client(message, conn, "eng")
    elif person[0] == 3:
        branch_arr = conn.execute("select name from BRANCH;").fetchall()
        son = 0
        for i in branch_arr:
            if message.text == i[0]:
                son = 1
                branch_id = conn.execute("select id from BRANCH where name = (?);", (i[0],)).fetchall()
                conn.execute("update CLIENT set branch = (?) where id = (?);", (branch_id[0][0], message.from_user.id))
                await food_menu.get_food_menu(message, conn, "eng", branch_id[0][0], True)
                break
        if son != 1:
            if message.text == "⬅️ Back":
                await delivery.get_delivery(message, conn, "eng")
    elif person[0] == 4:
        await callback_food_menu_uzb.get_callback(message, conn, person, "eng")
    elif person[0] == 5:
        await callback_food_uzb.get_callback(message, conn, person, "eng")
    elif person[0] == 6:
        await callback_uzb.get_callback(message, conn, person, "eng")
    elif person[0] == 10:
        conn.execute("update CLIENT set bosqich = 11 where id = (?);", (message.from_user.id,))
        await bot.send_message(message.from_user.id, "Enter your name:")
    elif person[0] == 11:
        await get_user_name(message, conn, "eng", vote_cb)
    elif person[0] == 13:
        await get_phone(message, conn, "eng")
