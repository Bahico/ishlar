from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from admin.menu.menu import admin_main_menu
from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def admin_contact(message:types.Message,admin_conn,conn,vote_cb):
    try: await bot.delete_message(message.from_user.id,message.message_id-1)
    except: pass
    await message.delete()
    admin_conn.execute(f"update USER set phone_number = (?), username = '{message.from_user.username}' where id = (?);",(message.contact.phone_number[1:],message.from_user.id))
    conn.execute("update SAVE set text = NULL where id = (?);",(message.from_user.id,))
    await message.answer("Qabul qilindi")
    await admin_main_menu(message, conn, vote_cb)