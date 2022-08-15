from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardButton, KeyboardButton

from config import TOKEN

# 'location', 'text', 'branch', 'language', 'action'
# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def get_photo(message: types.Message, conn, admin):
    admin = admin.split(',')
    conn.execute("insert into PHOTO (food_name,photo) values (?,?);",(admin[0],message.photo[0].file_id))
    conn.execute("update ADMIN set plus = NULL where id = (?);",(message.from_user.id,))
    await bot.send_message(message.from_user.id,"Qabul qilindi. 😊")
    conn.commit()
