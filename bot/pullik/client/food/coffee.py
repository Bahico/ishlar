from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from config import TOKEN

# 'location', 'text', 'branch', 'language', 'action'
# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def get_coffee(message: types.Message, conn,  language, branch):
    person = conn.execute("select basket from CLIENT where id = (?);", (message.from_user.id,)).fetchall()
    coffee = conn.execute("select coffee from BRANCH where id = (?);",(int(branch),)).fetchall()
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    person = list(person[0])
    if language == "uzb":
        son = 0
        coffee = coffee.split('.')
        markup.add(KeyboardButton(text="⬅️ Ortga"))
        if person[0] is not None:
            markup.add(KeyboardButton(text="📥 Savat"))
        for i in coffee:
            i = i.split(',')
            if i[0] == "True":
                son += 1
                markup.add(KeyboardButton(text=i[1]))
        if son != 1 and son != 0:
            await bot.send_message(message.from_user.id,"Nimadan boshlaymiz? 😊",reply_markup=markup)
        elif son == 1:
            await bot.send_message(message.from_user.id,"Bizda faqat bir xil coffee qolgan. 😑")

    elif language == "rus":
        son = 0
        coffee = coffee.split('.')
        markup.add(KeyboardButton(text="⬅️ Назад"))
        if person[0] is not None:
            markup.add(KeyboardButton(text="📥 Корзина"))
        for i in coffee:
            i = i.split(',')
            if i[0] == "True":
                son += 1
                markup.add(KeyboardButton(text=i[1]))
        if son != 1 and son != 0:
            await bot.send_message(message.from_user.id,"Nimadan boshlaymiz? 😊",reply_markup=markup)
        elif son == 1:
            await bot.send_message(message.from_user.id,"У нас остался только тот же кофе. 😑",reply_markup=markup)

    elif language == "eng":
        son = 0
        coffee = coffee.split('.')
        markup.add(KeyboardButton(text="⬅️ Back"))
        if person[0] is not None:
            markup.add(KeyboardButton(text="📥 Basket"))
        for i in coffee:
            i = i.split(',')
            if i[0] == "True":
                son += 1
                markup.add(KeyboardButton(text=i[1]))
        if son != 1 and son != 0:
            await bot.send_message(message.from_user.id,"Where to start? 😊",reply_markup=markup)
        elif son == 1:
            await bot.send_message(message.from_user.id,"We only have the same coffee left. 😑",reply_markup=markup)