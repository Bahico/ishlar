from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types

from bot.menu.main_menu import bot_main_menu
from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def bot_branch_all_arr(message: types.Message, conn, vote_cb, callback_query):
    branch = conn.execute("select name, id, admin from BRANCH;").fetchall()
    awa = ""
    if callback_query["language"] == "uzb":
        sons = 0
        for i in branch:
            sons += 1
            son = 0
            if i[2] is not None:
                for _ in i[2].split("."):
                    son += 1
                awa += str(sons) + ") \"" + i[0] + "\" dokonida " + str(son) + " ta admin bor\n"
            else:
                awa += str(sons) + ") \"" + i[0] + "\" dokonida adminlar yo'q"
    elif callback_query['language'] == "eng":
        sons = 0
        for i in branch:
            sons += 1
            son = 0
            if i[2] is not None:
                for _ in i[2].split("."):
                    son += 1
                #  Andijan somsa store has 5 admins
                awa += str(sons) + ") \"" + i[0] + "\" store has " + str(son) + " admins\n"
            else:
                awa += str(sons) + ") \"" + i[0] + "\" store has not admins\n"
    elif callback_query["language"] == "rus":
        sons = 0
        for i in branch:
            sons += 1
            son = 0
            if i[2] is not None:
                for _ in i[2].split("."):
                    son += 1
                awa += str(sons) + ") \"" + i[0] + "\" магазин имеет " + str(son) + " администраторов\n"
            else:
                awa += str(sons) + ") \"" + i[0] + "\" магазин имеет " + str(son) + " администраторов\n"

    await bot.send_message(message.from_user.id, awa)
    await bot_main_menu(message, vote_cb, callback_query["language"],conn)
