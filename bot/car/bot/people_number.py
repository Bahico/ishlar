from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types

from bot.menu.main_menu import bot_main_menu
from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def get_people_number(message:types.Message,conn,vote_cb,callback_query):
    people = conn.execute("select * from CLIENT;").fetchall()
    son = 0
    for i in people:
        son += 1

    if callback_query["language"] == "uzb":
        if son != 0:
            await bot.send_message(message.from_user.id,"Jami odam soni: "+str(son)+" ta")
        else:
            await bot.send_message(message.from_user.id,"Hali Foydalanuvchilar yo'q!")
    elif callback_query["language"] == "rus":
        if son != 0:
            await bot.send_message(message.from_user.id,"Общее количество людей: "+str(son))
        else:
            await bot.send_message(message.from_user.id,"Пользователей пока нет!")
    elif callback_query["language"] == "eng":
        if son != 0:
            await bot.send_message(message.from_user.id,"Total number of people: "+str(son))
        else:
            await bot.send_message(message.from_user.id,"No Users yet!")
    await bot_main_menu(message,vote_cb,callback_query["language"],conn)


# maxluqlar ligasi