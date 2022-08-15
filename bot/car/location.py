from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import ReplyKeyboardRemove

from branch.menu.main_menu import admin_branch_menu
from client.my_settings import client_location
from config import TOKEN

# some code

# "id", "language", "action"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def get_location(message: types.Message, conn, vote_cb):
    """
    Location oladi
    :param vote_cb:
    :param message:
    :param conn:
    :return: Eng yaqn filialni chiqarib beradi
    """
    branch = conn.execute("select branch, language from ADMIN where id = (?) and test = 4;",
                          (message.from_user.id,)).fetchall()
    client = conn.execute("select settings, language from CLIENT where id = (?);", (message.from_user.id,)).fetchall()
    if branch:
        conn.execute("update BRANCH set longitude = (?), latitude = (?) where id = (?);",
                     (message.location.longitude, message.location.latitude, branch[0][0]))
        await admin_branch_menu(message, conn, vote_cb, branch[0][1])
        await bot.send_message(message.from_user.id, "✅", reply_markup=ReplyKeyboardRemove())
    elif client and client[0][0] == "my_location":
        await client_location(message, conn, vote_cb, client[0][1])
