from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from config import TOKEN

# 'location', 'text', 'branch', 'language', 'action'
# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def get_fast_food(message: types.Message, conn, language, branch):
    person = conn.execute("select basket from CLIENT where id = (?);",(message.from_user.id,)).fetchall()
    fast_food = conn.execute("select fast_food from BRANCH where id = (?);",(int(branch),)).fetchall()
    conn.execute("update CLIENT set bosqich = 5 where id = (?);",(message.from_user.id,))
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    person = list(person[0])
    if language == "uzb":
        son = 0
        fast_food = fast_food[0][0].split('.')
        markup.add(KeyboardButton(text="⬅️ Ortga"))
        if person[0] is not None:
            markup.add(KeyboardButton(text="📥 Savat"))
        for i in fast_food:
            i = i.split(',')
            if i[0] == "True":
                son += 1
                markup.add(KeyboardButton(text=i[1]))

        if son != 1 and son != 0:
            await bot.send_message(message.from_user.id,"Nimadan boshlaymiz? 😉",reply_markup=markup)
        elif son == 1:
            await bot.send_message(message.from_user.id,"Bizda bir xil fast food qoldi. 🤭",reply_markup=markup)
    elif language == "rus":
        son = 0
        fast_food = fast_food.split('.')
        markup.add(KeyboardButton(text="⬅️ Назад"))
        if person[0] is not None:
            markup.add(KeyboardButton(text="📥 Корзина"))
        for i in fast_food:
            i = i.split(',')
            if i[0] == "True":
                son += 1
                markup.add(KeyboardButton(text=i[1]))

        if son != 1 and son != 0:
            await bot.send_message(message.from_user.id,"С чего начать покупки? 😉",reply_markup=markup)
        elif son == 1:
            await bot.send_message(message.from_user.id,"Мы остались с тем же фаст-фуд. 🤭",reply_markup=markup)

    if language == "eng":
        son = 0
        fast_food = fast_food.split('.')
        markup.add(KeyboardButton(text="⬅️ Back"))
        if person[0] is not None:
            markup.add(KeyboardButton(text="📥 Basket"))
        for i in fast_food:
            i = i.split(',')
            if i[0] == "True":
                son += 1
                markup.add(KeyboardButton(text=i[1]))

        if son != 1 and son != 0:
            await bot.send_message(message.from_user.id,"Where to start? 😉",reply_markup=markup)
        elif son == 1:
            await bot.send_message(message.from_user.id,"We were left with the same fast food. 🤭",reply_markup=markup)