from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types

from ..basket import basket_uz, basket_eng,basket_rus

from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def get_user_name(message: types.Message, conn, language, vote_cb):
    user_name = message.text
    son = 0
    for i in user_name:
        try:
            int(i)
            son = 1
        except:
            pass
    if language == "uzb":
        if son != 1:
            await bot.send_message(message.from_user.id,f"Salom {user_name}")
            conn.execute("update CLIENT set bosqich = (?), name = (?) where id = (?);",(12,user_name,message.from_user.id))
            await basket_uz.get_basket(message,conn,vote_cb)
        else:
            await bot.send_message(message.from_user.id,"Xato qayta kiriting.")
    elif language == "rus":
        if son != 1:
            await bot.send_message(message.from_user.id,f"Привет {user_name}")
            conn.execute("update CLIENT set bosqich = (?), name = (?) where id = (?);",(12,user_name,message.from_user.id))
            await basket_rus.get_basket(message,conn,vote_cb)
        else:
            await bot.send_message(message.from_user.id,"Ошибка. повторно введите.")
    elif language == "eng":
        if son != 1:
            await bot.send_message(message.from_user.id,f"Hello {user_name}")
            conn.execute("update CLIENT set bosqich = (?), name = (?) where id = (?);",(12,user_name,message.from_user.id))
            await basket_eng.get_basket(message,conn,vote_cb)
        else:
            await bot.send_message(message.from_user.id,"Error. re-enter.")