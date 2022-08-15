from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def get_delete_(message: types.Message, conn, vote_cb, callback_query):
    food = conn.execute(f"select {callback_query['location']} from BRANCH where id = (?);",
                        (callback_query["branch"],)).fetchall()
    if food[0]:
        food = food[0][0].split('.')
        son_ = None
        if len(food) == 1:
            conn.execute(f"update BRANCH set {callback_query['location']} = NULL where id = (?);",
                         (callback_query["branch"],)).fetchall()
            son_ = callback_query["text"]
        else:
            print(food)
            for i in food:
                i = i.split(',')
                if callback_query["text"] == i[0]:
                    son_ = i[0]
                    food.remove(i)
                    break
            print(food)
            awa = ''
            son = 0
            for i in food:
                if son == 0:
                    awa += i
                    son = 1
                else:
                    awa += "." + i
            if not food:
                conn.execute(f"update BRANCH set {callback_query['location']} = (?) where id = (?);",
                         (None, message.from_user.id))
            else:
                conn.execute(f"update BRANCH set {callback_query['location']} = (?) where id = (?);",
                         (awa, message.from_user.id))
        await bot.send_message(message.from_user.id, f"{son_} nomli maxsulot o'chirlidi.")
    else:
        await bot.send_message(message.from_user.id,"O'chirilgan")
