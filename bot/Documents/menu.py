from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types

from bot.menu.main_menu import bot_main_menu
from branch.menu.main_menu import admin_branch_menu
from client.menu.menu import client_menu
from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def get_menu(message: types.Message, conn, vote_cb):
    try:
        await bot.delete_message(message.from_user.id, message.message_id - 1)
    except:
        pass
    admin = conn.execute("select settings, language, branch, test from ADMIN where id = (?);",
                         (message.from_user.id,)).fetchall()
    client = conn.execute("select language from CLIENT where id = (?);", (message.from_user.id,)).fetchall()
    bot_ = conn.execute("select settings, language, name, login from I_ where id = (?);",
                        (message.from_user.id,)).fetchall()
    if bot_:
        await bot_main_menu(message, vote_cb, bot_[0][1], conn)
    elif admin and admin[0][3] == 4:
        await admin_branch_menu(message, conn, vote_cb, admin[0][1])
    elif client and client[0][0] is not None:
        await client_menu(message, vote_cb, client[0][0])
    else:
        conn.execute("delete from ADMIN where id = (?);", (message.from_user.id,))
        await bot.send_message(message.from_user.id, "Iltimos botdan to'g'ri maqsadda foydalaning")
