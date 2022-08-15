from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from ..food_settings import callback_uzb
from ..history.history import get_history
from ..main_menu import main_menu
from ..delivery import delivery
from ..food_menu import food_menu, callback_food_menu_uzb
from ..food import callback_food_uzb
from ..user.user_name import get_user_name
from ..phone_number.phone_number import get_phone

from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



async def get_message_uzb(message: types.Message, conn,vote_cb):
    person = conn.execute("select bosqich, basket, branch, tur, basket, comment from CLIENT where id = (?);",
                          (message.from_user.id,)).fetchall()
    person = list(person[0])
    if person[-1] is not None:
        if message.text != "STOP":
            await bot.send_message(person[-1],message.text)
        else:
            conn.execute("update CLIENT set comment = NULL where id = (?);",(message.from_user.id,))
            await bot.send_message(message.from_user.id,"Suxbat uchun rahmat😊")
    elif person[0] == 1:
        if message.text == "🍽 Menyu":
            await delivery.get_delivery(message, conn, "uzb")
        elif message.text == "📖 Buyurtmalar tarixi":
            await get_history(message,conn,"uzb")
        elif message.text == "✍️ Fikr bildirish":
            conn.execute("update CLIENT set comment = (?) where id = (?);",(735095740,message.from_user.id))
            markup = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("STOP"))
            await bot.send_message(message.from_user.id,"Yozishingiz mumkin\n\nYozib bo'lgach STOP tugmasini bosing",reply_markup=markup)
        elif message.text == "☎️ Biz bilan aloqa":
            await bot.send_message(message.from_user.id,"Agar sizda savollar bo'lsa bizga yozishingiz yoki qo'ng'iroq qilishingiz mumkin:\n📨@DwichuzAdmin\n📞+998974109750")
    elif person[0] == 2:
        if message.text == "🏃 Olib ketish":
            conn.execute("update CLIENT set delivery = (?), bosqich = 13 where id = (?);",
                         ("take", message.from_user.id))
            markup = ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(KeyboardButton("📱 Mening Telefon raqamim", request_contact=True))
            markup.add(KeyboardButton("⬅️ Ortga"))
        elif message.text == "⬅️ Ortga":
            await main_menu.get_menu_client(message, conn, "uzb")
    elif person[0] == 3:
        branch_arr = conn.execute("select name from BRANCH;").fetchall()
        son = 0
        for i in branch_arr:
            if message.text == i[0]:
                son = 1
                branch_id = conn.execute("select id from BRANCH where name = (?);", (i[0],)).fetchall()
                conn.execute("update CLIENT set branch = (?) where id = (?);", (branch_id[0][0], message.from_user.id))
                await food_menu.get_food_menu(message, conn, "uzb", branch_id[0][0], True)
                break
        if son != 1:
            if message.text == "⬅️ Ortga":
                await delivery.get_delivery(message, conn, "uzb")
    elif person[0] == 4:
        await callback_food_menu_uzb.get_callback(message, conn, person, "uzb")
    elif person[0] == 5:
        await callback_food_uzb.get_callback(message, conn, person, "uzb")
    elif person[0] == 6:
        await callback_uzb.get_callback(message, conn, person, "uzb")
    elif person[0] == 10:
        conn.execute("update CLIENT set bosqich = 11 where id = (?);", (message.from_user.id,))
        await bot.send_message(message.from_user.id, "Ismingizni kiriting:")
    elif person[0] == 11:
        await get_user_name(message, conn, "uzb",vote_cb)
    elif person[0] == 13:
        await get_phone(message, conn,"uzb")
