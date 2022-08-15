from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import ReplyKeyboardRemove

from config import TOKEN

# some code
from family.menu.menu import family_main_menu

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



async def family_contact(message:types.Message,family_conn,conn,vote_cb):
    try: await bot.delete_message(message.from_user.id,message.message_id-1)
    except: pass
    await message.delete()
    family_conn.execute(f"insert into CONN(id, phone_number, username) values (?,?,'{message.from_user.username}');",(message.from_user.id,message.contact.phone_number[1:]))
    conn.execute("update SAVE set text NULL where id = (?);",(message.from_user.id,))
    await message.answer("Qabul qilindi",reply_markup=ReplyKeyboardRemove())
    await family_main_menu(message, conn, vote_cb)