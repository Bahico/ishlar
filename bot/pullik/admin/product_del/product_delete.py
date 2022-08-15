from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def get_delete(message: types.Message, conn, vote_cb, callback_query):
    food = conn.execute(f"select {callback_query['location']} from BRANCH where id = (?);", (callback_query["branch"],)).fetchall()
    markup = InlineKeyboardMarkup(resize_keyboard=True)
    food = food[0]
    food = food[0].split(".")
    son = 0
    for i in food:
        son = 1
        i = i.split(',')
        if i[0] == "True":
            markup.insert(InlineKeyboardButton(text="🟢 " + i[1],
                                               callback_data=vote_cb.new(location=callback_query["text"], text=i[1],
                                                                         branch=callback_query["branch"], language="--",
                                                                         action="admin")))
        else:
            markup.insert(InlineKeyboardButton(text="🔴 " + i[1],
                                               callback_data=vote_cb.new(location=callback_query["text"], text=i[1],
                                                                         branch=callback_query["branch"], language="--",
                                                                         action="admin")))
    if son == 1:
        await bot.send_message(message.from_user.id, "Qaysi turdagi maxsulot o'chirish kerak?", reply_markup=markup)
    else:
        await bot.send_message(message.from_user.id, "Bu turdagi maxsulotlarni hammasi o'chirilgan.")


async def get_product_del(message: types.Message, conn, callback_query):
    food = conn.execute(f"select {callback_query['location']} from BRANCH where id = (?);",
                        (callback_query["branch"]), ).fetchall()
    markup = InlineKeyboardMarkup(resize_keyboard=True)
    food = food[0]
    food = food[0].split(".")
    son = 0
    for i in food:
        son = 1
        i = i.split(',')
        if i[1] == callback_query["text"]:
            ig = f"{i[0]},{i[1]},{i[2]}"
            food.remove(ig)
            if i[0] == "True":
                i[0] = "False"
            else:
                i[0] = "True"
            i = f"{i[0]},{i[1]},{i[2]}"
            food.append(i)
    awa = ""
    son = 0
    for i in food:
        if son == 0:
            awa += i
            son = 1
        else:
            awa += ")" + i
    conn.execute(f"update BRANCH set {callback_query['location']} = ({awa}) where id = {callback_query['branch']}")
    await bot.send_message(message.from_user.id, "Qabul qilindi.")