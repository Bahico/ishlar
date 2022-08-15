from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types

from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def get_logout(message:types.Message,governor_conn,district_conn,director_conn,admin_conn,teacher_conn,family_conn,conn):
    await message.delete()
    governor_conn.execute("delete from USER where id = (?);",(message.from_user.id,))
    governor_conn.execute("delete from SAVE where id = (?);",(message.from_user.id,))
    district_conn.execute("delete from USER where id = (?);",(message.from_user.id,))
    district_conn.execute("delete from SAVE where id = (?);",(message.from_user.id,))
    director_conn.execute("delete from USER where id = (?);",(message.from_user.id,))
    director_conn.execute("delete from SAVE where id = (?);",(message.from_user.id,))
    admin_conn.execute("delete from USER where id = (?);",(message.from_user.id,))
    admin_conn.execute("delete from SAVE where id = (?);",(message.from_user.id,))
    family_conn.execute("delete from SAVE where id = (?);",(message.from_user.id,))
    family_conn.execute("delete from CONN where id = (?);",(message.from_user.id,))
    family_conn.execute("delete from CHILDREN where id = (?);",(message.from_user.id,))
    conn.execute("delete from SAVE where id = (?);",(message.from_user.id,))
    teacher_conn.execute("delete from USER where id = (?);",(message.from_user.id,))
    teacher_conn.execute("delete from FAN where id = (?);",(message.from_user.id,))
    governor_conn.commit(),district_conn.commit(),director_conn.commit(),admin_conn.commit(),teacher_conn.commit(),family_conn.commit(),conn.commit()
    await bot.send_message(message.from_user.id,"Siz botdan o'chirildingiz")