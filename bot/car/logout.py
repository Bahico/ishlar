from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types

from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def get_logout_message(message: types.Message, conn):
    admin = conn.execute("select * from ADMIN where id = (?);", (message.from_user.id,)).fetchall()
    if admin:
        conn.execute("delete from ADMIN where id = (?);", (message.from_user.id,))
        await bot.send_message(message.from_user.id, "Siz admin ro'yxatidan o'chirildingiz.")
    client = conn.execute("select * from CLIENT where id = (?);", (message.from_user.id,)).fetchall()
    if client:
        conn.execute("delete from CLIENT where id = (?);", (message.from_user.id,))
        await bot.send_message(message.from_user.id, "Siz client ro'yxatidan o'chirildingiz.")
    bot_ = conn.execute("select * from I_ where id = (?);", (message.from_user.id,)).fetchall()
    if bot_:
        conn.execute("delete from I_ where id = (?);", (message.from_user.id,))
        await bot.send_message(message.from_user.id, "clear")
