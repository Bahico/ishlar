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


async def get_message_rus(message: types.Message, conn,vote_cb):
    person = conn.execute("select bosqich, basket, branch, tur, basket, comment from CLIENT where id = (?);",
                          (message.from_user.id,)).fetchall()
    person = list(person[0])
    if person[-1] is not None:
        if message.text != "STOP":
            await bot.send_message(person[-1],message.text)
        else:
            conn.execute("update CLIENT set comment = NULL where id = (?);",(message.from_user.id,))
            await bot.send_message(message.from_user.id,"Спасибо за чат😊")
    elif person[0] == 1:
        if message.text == "🍽 Меню":
            await delivery.get_delivery(message, conn, "rus")
        elif message.text == "📖 История заказов":
            await get_history(message,conn,"rus")
        elif message.text == "✍️ Дать обратную связь":
            conn.execute("update CLIENT set comment = (?) where id = (?);",())
            markup = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("STOP"))
            await bot.send_message(message.from_user.id,"Ты можешь написать\n\nКогда вы закончите запись, нажмите кнопку STOP",reply_markup=markup)
        elif message.text == "☎️ Связаться с нами":
            await bot.send_message(message.from_user.id,"Если у вас есть вопросы, вы можете написать или позвонить нам:\n📨@   \n📞+998974109750")
    elif person[0] == 2:
        if message.text == "🏃 Забрать":
            conn.execute("update CLIENT set delivery = (?), bosqich = 13 where id = (?);",
                         ("take", message.from_user.id))
            markup = ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(KeyboardButton("📱 Мой номер телефона", request_contact=True))
            markup.add(KeyboardButton("⬅️ Назад"))
        elif message.text == "⬅️ Назад":
            await main_menu.get_menu_client(message, conn, "rus")
    elif person[0] == 3:
        branch_arr = conn.execute("select name from BRANCH;").fetchall()
        son = 0
        for i in branch_arr:
            if message.text == i[0]:
                son = 1
                branch_id = conn.execute("select id from BRANCH where name = (?);", (i[0],)).fetchall()
                conn.execute("update CLIENT set branch = (?) where id = (?);", (branch_id[0][0], message.from_user.id))
                await food_menu.get_food_menu(message, conn, "rus", branch_id[0][0], True)
                break
        if son != 1:
            if message.text == "⬅️ Назад":
                await delivery.get_delivery(message, conn, "rus")
    elif person[0] == 4:
        await callback_food_menu_uzb.get_callback(message, conn, person, "rus")
    elif person[0] == 5:
        await callback_food_uzb.get_callback(message, conn, person, "rus")
    elif person[0] == 6:
        await callback_uzb.get_callback(message, conn, person, "rus")
    elif person[0] == 10:
        conn.execute("update CLIENT set bosqich = 11 where id = (?);", (message.from_user.id,))
        await bot.send_message(message.from_user.id, "Введите ваше имя:")
    elif person[0] == 11:
        await get_user_name(message, conn, "rus",vote_cb)
    elif person[0] == 13:
        await get_phone(message, conn,"rus")
