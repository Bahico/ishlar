from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from config import TOKEN

# 'location', 'text', 'branch', 'language', 'action'
# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def get_waffle(message: types.Message, conn, language, branch):
    person = conn.execute("select basket from CLIENT where id = (?);",(message.from_user.id,)).fetchall()
    waffle = conn.execute(f"select waffle from BRANCH where id = (?);",(int(branch),)).fetcahll()
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    person = list(person[0])
    if language == "uzb":
        son = 0
        markup.add(KeyboardButton(text="⬅️ Orqaga"))
        if person[0] is not None:
            markup.add(KeyboardButton(text="📥 Savat"))
        waffle = waffle[0].split('.')
        for i in waffle:
            i = i.split(',')
            if i[0] == "True":
                son += 1
                markup.add(KeyboardButton(text=i[1]))
        if son != 1 and son != 0:
            await bot.send_message(message.from_user.id,"Nimadan boshlaymiz? 😁",reply_markup=markup)
        elif son == 1:
            await bot.send_message(message.from_user.id,"Bizda bir xil vaflilar qoldi. 😐",reply_markup=markup)
        elif son == 0:
            await bot.send_message(message.from_user.id,"Hozircha waflilar qolmadi. 😔",reply_markup=markup)
    elif language == "rus":
        son = 0
        markup.add(KeyboardButton(text="⬅️ Назад"))
        if person[0] is not None:
            markup.add(KeyboardButton(text="📥 Корзина"))
        waffle = waffle[0].split('.')
        for i in waffle:
            i = i.split(',')
            if i[0] == "True":
                son += 1
                markup.add(KeyboardButton(text=i[1]))
        if son != 1 and son != 0:
            await bot.send_message(message.from_user.id,"Nimadan boshlaymiz? 😁",reply_markup=markup)
        elif son == 1:
            await bot.send_message(message.from_user.id,"Мы остались с теми же вафлями. 😐",reply_markup=markup)
        elif son == 0:
            await bot.send_message(message.from_user.id,"Вафли пока не осталось. 😔")
    elif language == "eng":
        son = 0
        markup.add(KeyboardButton(text="⬅️ Back"))
        if person[0] is not None:
            markup.add(KeyboardButton(text="📥 Basket"))
        waffle = waffle[0].split('.')
        for i in waffle:
            i = i.split(',')
            if i[0] == "True":
                son += 1
                markup.add(KeyboardButton(text=i[1]))
        if son != 1 and son != 0:
            await bot.send_message(message.from_user.id,"Nimadan boshlaymiz? 😁",reply_markup=markup)
        elif son == 1:
            await bot.send_message(message.from_user.id,"We only have the same waffles left. 😐",reply_markup=markup)
        elif son == 0:
            await bot.send_message(message.from_user.id,"So far no waffles left. 😔")
