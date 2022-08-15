
from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from ..main_menu.main_menu import get_menu_client
from ..send_admin.send_admin import get_send_admin

from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def get_callback_client(message: types.Message, conn, callback_query, vote_cb):
    if callback_query["location"] == "all_del":
        conn.execute("update CLIENT set basket = NULL where id = (?);", (message.from_user.id,))
        await get_menu_client(message, conn, callback_query["language"])
    elif callback_query["location"] == "delivery":
        await get_send_admin(message,conn,callback_query["language"])
    elif callback_query["location"] == "back":
        await get_menu_client(message, conn, callback_query["language"])
    elif callback_query["location"] == "/":
        person = conn.execute("select basket from CLIENT where id = (?);",
                                  (message.from_user.id,)).fetchall()
        person = person[0]
        awa = ""
        foods = person[0].split('.')
        for i in foods:
            food = i.split(",")
            if food[1] == callback_query['location']:
                pass
            else:
                awa = food[0] + ',' + food[1] + ',' + food[2]
        if awa != "":
            conn.execute("update CLIENT set basket = (?) where id = (?);",(awa,message.from_user.id))
        else:
            conn.execute("update CLIENT set basket = NULL where id = (?);",(message.from_user.id,))
        await get_print(message,conn,vote_cb,callback_query)
    else:
        if callback_query["text"] == "+":
            person = conn.execute("select basket from CLIENT where id = (?);",
                                  (message.from_user.id,)).fetchall()
            person = person[0]
            if person[0] is not None:
                awa = ""
                foods = person[0].split('.')
                for i in foods:
                    food = i.split(",")
                    if food[1] == callback_query['location']:
                        food_ = int(food[2]) + 1
                        if food_ <= 0:
                            pass
                        else:
                            awa = food[0] + ',' + food[1] + ',' + str(food_)
                    else:
                        awa = food[0] + ',' + food[1] + ',' + food[2]
                if awa != "":
                    conn.execute("update CLIENT set basket = (?) where id = (?);",(awa,message.from_user.id))
                else:
                    conn.execute("update CLIENT set basket = NULL where id = (?);",(awa,message.from_user.id))
                await get_print(message,conn,vote_cb,callback_query)
            else:
                await bot.send_message(message.from_user.id,"Savat bo'sh")
                await get_menu_client(message,conn,"uzb")
        elif callback_query["text"] == "-":
            person = conn.execute("select basket from CLIENT where id = (?);",
                                  (message.from_user.id,)).fetchall()
            person = person[0]
            if person[0] is not None:
                awa = ""
                foods = person[0].split('.')
                for i in foods:
                    food = i.split(",")
                    if food[1] == callback_query['location']:
                        food_ = int(food[2]) - 1
                        if food_ <= 0:
                            pass
                        else:
                            awa = food[0] + ',' + food[1] + ',' + str(food_)
                    else:
                        awa = food[0] + ',' + food[1] + ',' + food[2]
                if awa != "":
                    conn.execute("update CLIENT set basket = (?) where id = (?);",(awa,message.from_user.id))
                else:
                    conn.execute("update CLIENT set basket = NULL where id = (?);",(message.from_user.id,))
                await get_print(message,conn,vote_cb,callback_query)
            else:
                await bot.send_message(message.from_user.id,"Savat bo'sh")
                await get_menu_client(message,conn,"uzb")
        elif callback_query["text"] == "/":
            person = conn.execute("select basket from CLIENT where id = (?);",
                                  (message.from_user.id,)).fetchall()
            person = person[0]
            if person[0] is not None:
                awa = ""
                foods = person[0].split('.')
                for i in foods:
                    food = i.split(",")
                    print(food[1], callback_query["location"])
                    if food[1] != callback_query['location']:
                        awa = food[0] + ',' + food[1] + ',' + food[2]
                if awa != "":
                    conn.execute("update CLIENT set basket = (?) where id = (?);",(awa,message.from_user.id))
                else:
                    conn.execute("update CLIENT set basket = NULL where id = (?);",(message.from_user.id,))
                await get_print(message,conn,vote_cb,callback_query)
            else:
                await bot.send_message(message.from_user.id,"Savat bo'sh")
                await get_menu_client(message,conn,"uzb")



async def get_print(message: types.Message, conn, vote_cb, callback_query):
    person = conn.execute("select basket, branch from CLIENT where id = (?);", (message.from_user.id,)).fetchall()
    person = person[0]
    if person[0] is not None:
        foods = person[0].split('.')
        awa = "Savat:\n\n"
        all_summa = 0
        markup = InlineKeyboardMarkup(resize_keybord=True)
        for i in foods:
            food = i.split(",")
            if food[1] == callback_query['location']:
                food_del = food[0] + ',' + food[1] + ',' + food[2]
                foods.remove(food_del)
                food_ = int(food[2]) - 1
                food[2] = str(food_)
                foods.append(food_del)
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
        await bot.send_message(message.from_user.id, awa, reply_markup=markup)
    else:
        await bot.send_message(message.from_user.id,"Savat bo'sh")
        await get_menu_client(message,conn,"uzb")
    await bot.delete_message(message.from_user.id, message.message.message_id)
