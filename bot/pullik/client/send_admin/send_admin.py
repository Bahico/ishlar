import datetime

from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def get_send_admin(message: types.Message, conn, language):
    person = conn.execute("select branch, basket, latitude, longitude, phone_number, received from CLIENT where id = (?);", (message.from_user.id,)).fetchall()
    person = person[0]
    admins = conn.execute("select id from ADMIN where branch = (?);", (person[0],)).fetchall()
    foods = person[0].split('.')
    if language == "uzb":
        awa = "Savat:\n\n"
        all_summa = 0
        markup = InlineKeyboardMarkup(resize_keybord=True)
        for i in foods:
            food = i.split(",")
            if len(food) == 3:
                food_number = None
                food_ = conn.execute(f"select {food[0]} from BRANCH where id = (?);", (person[1],)).fetchall()
                food_ = food_[0][0].split('.')
                for i in food_:
                    i = i.split(',')
                    if i[1] == food[1]:
                        food_number = i[2]
                summa = int(food[2]) * int(food_number)
                all_summa += summa
                awa += food[0] + "\n" + food[1] + "\n" + food[2] + " x " + food_number + f" ({str(summa)} so'm)\n\n"
        awa += "Summa: " + str(all_summa) + "so'm\n\n"
        awa += "Telefon raqami:+998"+str(person[4])
        for i in admins:
            son = 0
            if person[2] is not None:
                await bot.send_location(i[0],person[2],person[3])
                son = 1
            if son == 1:
                await bot.send_message(i[0],f"Olib borish kerak.🚖\n\n{awa}")
            else:
                await bot.send_message(i[0],f"O'zi olib ketadi.🏃\n\n{awa}")
        if person[-1] is None:
            conn.execute("update CLIENT set received = (?) where id = (?);",(person[1],message.from_user.id))
        else:
            conn.execute("update CLIENT set received = (?) where id = (?);",(person[-1]+")"+person[1]+","+person[0]+","+datetime.datetime.now().strftime("%x"),message.from_user.id))