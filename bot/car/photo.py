from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types

from branch.menu.main_menu import admin_branch_menu
from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def get_photo(message:types.Message,conn,vote_cb):
    await message.delete()
    admin = conn.execute("select settings, language from ADMIN where id = (?);",(message.from_user.id,)).fetchall()
    admin_ = conn.execute("select spare from ADMIN_ where id = (?);",(message.from_user.id,)).fetchall()
    if admin and admin[0][0].split(",")[0] == 'spare photo':
        conn.execute("insert into PHOTO(id,type,photo) values (?,'spare',?);",(int(admin_[0][0]),message.photo[0].file_id))
        await message.answer("✅✅")
        await admin_branch_menu(message,conn,vote_cb,admin[0][1])
        await bot.delete_message(message.from_user.id,message.message_id+1)
        conn.execute("update ADMIN set settings = 0 where id = (?);",(message.from_user.id,))