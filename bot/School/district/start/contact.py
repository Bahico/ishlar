from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove

from config import TOKEN

# some code
from district.menu.menu import district_main_menu

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



async def district_contact(message:types.Message,district_conn,conn,vote_cb):
    try: await bot.delete_message(message.from_user.id,message.message_id-1)
    except: pass
    await message.delete()
    district_conn.execute(f"update USER set phone_number = (?), username = '{message.from_user.username}' where id = (?);",(message.contact.phone_number[1:],message.from_user.id))
    conn.execute("update SAVE set text = NULL where id = (?);",(message.from_user.id,))
    await message.answer("Qabul qilindi✅",reply_markup=ReplyKeyboardRemove())
    await district_main_menu(message, conn, vote_cb)