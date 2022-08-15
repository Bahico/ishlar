from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from config import TOKEN

# 'location', 'text', 'branch', 'language', 'action'
# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def get_start_admin(message: types.Message, conn):
    conn.execute("delete from ADMIN where id = (?);",(message.from_user.id,))
    conn.execute("delete from CLIENT where id = (?);",(message.from_user.id,))
    conn.execute("insert into ADMIN(id,bosqich) values (?,?);",(message.from_user.id,1))
    branch = conn.execute("select name, id from BRANCH;").fetchall()
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    son = 0
    for i in branch:
        son += 1
        markup.add(KeyboardButton(text=i[0]))
    if son > 1:
        await bot.send_message(message.from_user.id,"Qaysi flial",reply_markup=markup)
    elif son == 1:
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(KeyboardButton(text="Buyurtma qabul qilish"))
        markup.add(KeyboardButton(text="Ovqat kiritish"))
        await bot.send_message(message.from_user.id,"Tanlang👇👇",reply_markup=markup)
    else:
        await bot.send_message(message.from_user.id,"Xali filial qo'shilmagan.")