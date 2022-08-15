import sqlite3

from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types

from bot.menu.main_menu import bot_main_menu
from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def get_branch_add_name(message: types.Message, conn: sqlite3.Connection, callback_query: dict):
    conn.execute("update I_ set settings = 'add_branch_name' where id = (?);", (message.from_user.id,))
    if callback_query["language"] == "uzb":
        await bot.send_message(message.from_user.id, "Qo'shiladigon filial nomini kirting.")
    elif callback_query["language"] == "rus":
        await bot.send_message(message.from_user.id, "Введите название добавляемой ветки.")
    elif callback_query["language"] == "eng":
        await bot.send_message(message.from_user.id, "Enter the name of the branch to be added.")


async def get_branch_add_login(message: types.Message, conn, bot_):
    await bot.delete_message(message.from_user.id,message.message_id-1)
    conn.execute(f"update I_ set settings = 'add_branch_login', name = '{message.text}' where id = (?);",(message.from_user.id,))
    if bot_[1] == "uzb":
        await bot.send_message(message.from_user.id, "Qo'shiladigon filialning \"login\" inini kiriting.")
    elif bot_[1] == "rus":
        await bot.send_message(message.from_user.id, "Введите \"логин\" добавленной ветки.")
    elif bot_[1] == "eng":
        await bot.send_message(message.from_user.id, "Enter the \"login\" of the branch to be added.")



async def get_branch_add_code(message: types.Message, conn, bot_):
    await bot.delete_message(message.from_user.id,message.message_id-1)
    if bot_[1] == "uzb":
        branch = conn.execute(f"select * from BRANCH where login = '{message.text}';").fetchall()
        if not branch:
            conn.execute(f"update I_ set settings = 'add_branch_code', login = '{message.text}' where id = (?);",(message.from_user.id,))
            await bot.send_message(message.from_user.id, "Qo'shiladigon filialning \"code\" ini kiriting.")
        else:
            await bot.send_message(message.from_user.id,message.text+" loginlik filial bor qayta urining!")
    elif bot_[1] == "rus":
        branch = conn.execute(f"select * from BRANCH where login = '{message.text}';").fetchall()
        if not branch:
            conn.execute(f"update I_ set settings = 'add_branch_code', login = '{message.text}' where id = (?);",(message.from_user.id,))
            await bot.send_message(message.from_user.id, "Введите ветку \"код\" для добавления.")
        else:
            await bot.send_message(message.from_user.id,message.text+" попробуйте еще раз, есть раздел входа!")

    elif bot_[1] == "eng":
        branch = conn.execute(f"select * from BRANCH where login = '{message.text}';").fetchall()
        if not branch:
            conn.execute(f"update I_ set settings = 'add_branch_code', login = '{message.text}' where id = (?);",(message.from_user.id,))
            await bot.send_message(message.from_user.id, "Enter the code \"branch \" to be added.")
        else:
            await bot.send_message(message.from_user.id,message.text+" try again there is a login branch!")



async def get_branch_add_branch(message: types.Message, conn, vote_cb, bot_):
    await bot.delete_message(message.from_user.id,message.message_id-1)
    conn.execute("insert into BRANCH(name,login,code) values (?,?,?);", (bot_[2], bot_[3], message.text))
    conn.execute("update I_ set settings = NULL, name = NULL, login = NULL where id = (?);",(message.from_user.id,))
    if bot_[1] == "uzb":
        await bot.send_message(message.from_user.id,f"{bot_[2]} nomli filial yaratildi✅\n\nlogin:{bot_[3]}\ncode:{message.text}")
        await bot_main_menu(message, vote_cb, bot_[1],conn)
    elif bot_[1] == "rus":
        await bot.send_message(message.from_user.id,f"Создана ветка с именем {bot_[2]}✅\n\nлогин:{bot_[3]}\nкод:{message.text}")
        await bot_main_menu(message, vote_cb, bot_[1],conn)
    elif bot_[1] == "eng":
        await bot.send_message(message.from_user.id,f"A branch named {bot_[2]} has been created✅\n\nlogin:{bot_[3]}\ncode:{message.text}")
        await bot_main_menu(message, vote_cb, bot_[1],conn)
