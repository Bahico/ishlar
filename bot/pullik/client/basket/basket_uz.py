from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def get_basket(message: types.Message, conn, vote_cb):
    person = conn.execute("select basket, language, branch from CLIENT where id = (?);",(message.from_user.id,)).fetchall()
    person = person[0]
    if person[1] == "uzb":
        foods = person[0].split('.')
        awa = "Savat:\n\n"
        all_summa = 0
        markup = InlineKeyboardMarkup(resize_keybord=True)
        for i in foods:
            food = i.split(",")
            if len(food) == 3:
                food_number = None
                food_ = conn.execute(f"select {food[0]} from BRANCH where id = (?);", (person[2],)).fetchall()
                food_ = food_[0][0].split('.')
                for i in food_:
                    i = i.split(',')
                    if i[1] == food[1]:
                        food_number = i[2]
                summa = int(food[2]) * int(food_number)
                all_summa += summa
                awa += food[0] + "\n" + food[1] + "\n" + food[2] + " x " + food_number + f" ({str(summa)} so'm)\n\n"
                markup.row(InlineKeyboardButton(text=food[1],
                                                callback_data=vote_cb.new(location="None", text="None", branch="None",
                                                                          language="uzb", action="client")),
                           InlineKeyboardButton(text="+",
                                                callback_data=vote_cb.new(location=food[1], text="+", branch="None",
                                                                          language="uzb", action="client")),
                           InlineKeyboardButton(text="-",
                                                callback_data=vote_cb.new(location=food[1], text="-", branch="None",
                                                                          language="uzb", action="client")),
                           InlineKeyboardButton(text="🗑",
                                                callback_data=vote_cb.new(location=food[1], text="/", branch="None",
                                                                          language="uzb", action="client")))
        awa += "Umumiy: " + str(all_summa) + " so'm"
        markup.add(InlineKeyboardButton(text="🔄 Tozalash",
                                        callback_data=vote_cb.new(location="all_del", text="-", branch="None",
                                                                  language="uzb", action="client")))
        markup.add(InlineKeyboardButton(text="🚖 Buyurtma berish",
                                        callback_data=vote_cb.new(location="delivery", text="now", branch="None",
                                                                  language="uzb", action="client")))
        markup.add(InlineKeyboardButton(text="⬅️ Orqaga",
                                        callback_data=vote_cb.new(location="back", text="main_menu", branch="None",
                                                                  language="uzb", action="client")))
        await bot.send_message(message.from_user.id,awa,reply_markup=markup)