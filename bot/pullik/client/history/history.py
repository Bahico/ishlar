from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

# 'location', 'text', 'branch', 'language', 'action'
# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def get_history(message: types.Message, conn, language):
    person = conn.execute("select received from CLIENT where id = (?);",(message.from_user.id,)).fetchall()
    person = person[0]
    son = 0
    history = None
    if person[0] is not None:
        history = person[0].split(")")
    else:
        son = 1
        await bot.send_message(message.from_user.id,"Bosh🙁")
    awa = ""
    if son == 0:
        if language == "uzb":
            for i in history:
                foods = person[0].split('.')
                awa = "Savat:\n\n"
                all_summa = 0
                for i in foods:
                    food = i.split(",")
                    if len(food) == 3:
                        food_number = None
                        food_ = conn.execute(f"select {food[0]} from BRANCH where id = (?);", (food[-2],)).fetchall()
                        food_ = food_[0][0].split('.')
                        for i in food_:
                            i = i.split(',')
                            if i[1] == food[1]:
                                food_number = i[2]
                        summa = int(food[2]) * int(food_number)
                        all_summa += summa
                        awa += food[0] + "\n" + food[1] + "\n" + food[2] + " x " + food_number + f" ({str(summa)} so'm) {food[-1]} kuni\n\n"
                await bot.send_message(message.from_user.id,awa)
        elif language == "rus":
            for i in history:
                foods = person[0].split('.')
                awa = "Kорзина:\n\n"
                all_summa = 0
                for i in foods:
                    food = i.split(",")
                    if len(food) == 3:
                        food_number = None
                        food_ = conn.execute(f"select {food[0]} from BRANCH where id = (?);", (food[-2],)).fetchall()
                        food_ = food_[0][0].split('.')
                        for i in food_:
                            i = i.split(',')
                            if i[1] == food[1]:
                                food_number = i[2]
                        summa = int(food[2]) * int(food_number)
                        all_summa += summa
                        awa += food[0] + "\n" + food[1] + "\n" + food[2] + " x " + food_number + f" ({str(summa)} so'm) {food[-1]} день\n\n"
                await bot.send_message(message.from_user.id,awa)
        elif language == "eng":
            for i in history:
                foods = person[0].split('.')
                awa = "Basket:\n\n"
                all_summa = 0
                for i in foods:
                    food = i.split(",")
                    if len(food) == 3:
                        food_number = None
                        food_ = conn.execute(f"select {food[0]} from BRANCH where id = (?);", (food[-2],)).fetchall()
                        food_ = food_[0][0].split('.')
                        for i in food_:
                            i = i.split(',')
                            if i[1] == food[1]:
                                food_number = i[2]
                        summa = int(food[2]) * int(food_number)
                        all_summa += summa
                        awa += food[0] + "\n" + food[1] + "\n" + food[2] + " x " + food_number + f" ({str(summa)} so'm) {food[-1]} day\n\n"
                await bot.send_message(message.from_user.id,awa)