from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import ReplyKeyboardRemove

from config import TOKEN

# some code
from director.menu.menu import director_main_menu

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def director_contact(message:types.Message, conn, director_conn, vote_cb):
    try: await bot.delete_message(message.from_user.id,message.message_id-1)
    except: pass
    await message.delete()
    director_conn.execute(f"update USER set phone_number = (?), username = (?) where id = (?);",(message.contact.phone_number[1:],message.from_user.username,message.from_user.id,))
    conn.execute("update SAVE set text = NULL where id = (?);",(message.from_user.id,))
    await message.answer("Qabul qilindi",reply_markup=ReplyKeyboardRemove())
    await director_main_menu(message, conn, vote_cb)