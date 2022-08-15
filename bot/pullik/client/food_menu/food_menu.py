from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from config import TOKEN

# 'location', 'text', 'branch', 'language', 'action'

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def get_food_menu(message: types.Message, conn, language, branch, true):
    conn.execute("update CLIENT set bosqich = (?) where id = (?);",(4,message.from_user.id))
    person = conn.execute("select basket from CLIENT where id = (?);",(message.from_user.id,)).fetchall()
    menu = conn.execute("select * from BRANCH where id= (?);", (branch,)).fetchall()
    menu = list(menu[0])
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    person = person[0]
    son_ = 0
    if language == "uzb":
        if person[0] is not None:
            markup.add(KeyboardButton(text="📥 Savat"))
            markup.add(KeyboardButton(text="✅ Savatni to’ldirdim"))
        if menu[3] is not None:
            waffle = menu[5].split('.')
            son = 0
            for i in waffle:
                i = i.split(',')
                if i[0] == "True":
                    son = 1
                    son_ = 1
            if son == 1:
                markup.add(KeyboardButton(text="🧇 Vaflilar"))

        if menu[3] is not None:
            drinks = menu[3].split('.')
            son = 0
            for i in drinks:
                i = i.split(',')
                if i[0] == "True":
                    son = 1
                    son_ = 1
            if son == 1:
                markup.add(KeyboardButton(text="🧃 Salqin ichimliklar"))

        if menu[2] is not None:
            coffee = menu[2].split('.')
            son = 0
            for i in coffee:
                i = i.split(',')
                if i[0] == "True":
                    son = 1
                    son_ = 1
            if son == 1:
                markup.add(KeyboardButton(text="☕️ Coffee"))

        if menu[1] is not None:
            fast_food = menu[1].split('.')
            son = 0
            for i in fast_food:
                i = i.split(',')
                if i[0] == "True":
                    son = 1
                    son_ = 1
            if son == 1:
                markup.add(KeyboardButton(text="🍔️ Fast Food"))
        if son_ == 1:
            await bot.send_message(message.from_user.id,"Nimadan boshlaymiz?",reply_markup=markup)
        else:
            await bot.send_message(message.from_user.id,"Xozirda barcha maxsulotlar tugagan! 😔")

    elif language == "rus":
        if person[0] is not None:
            markup.add(KeyboardButton(text="📥 Корзина"))
            markup.add(KeyboardButton(text="✅ я наполнил корзину"))
        son_ = 0
        if menu[3] is not None:
            waffle = menu[5].split('.')
            son = 0
            for i in waffle:
                i = i.split(',')
                if i[0] == "True":
                    son = 1
                    son_ = 1
            if son == 1:
                markup.add(KeyboardButton(text="🧇 Вафли"))

        if menu[3] is not None:
            drinks = menu[3].split('.')
            son = 0
            for i in drinks:
                i = i.split(',')
                if i[0] == "True":
                    son = 1
                    son_ = 1
            if son == 1:
                markup.add(KeyboardButton(text="🧃 Прохладительные напитки"))

        if menu[2] is not None:
            coffee = menu[2].split('.')
            son = 0
            for i in coffee:
                i = i.split(',')
                if i[0] == "True":
                    son = 1
                    son_ = 1
            if son == 1:
                markup.add(KeyboardButton(text="☕️ Coffee"))

        if menu[1] is not None:
            fast_food = menu[1].split('.')
            son = 0
            for i in fast_food:
                i = i.split(',')
                if i[0] == "True":
                    son = 1
                    son_ = 1
            if son == 1:
                markup.add(KeyboardButton(text="🍔️️ Быстрое питание"))
        if son_ == 1:
            if true == 1:
                await bot.send_message(message.from_user.id,"Начнем с того, что получаем?",reply_markup=markup)
        else:
            await bot.send_message(message.from_user.id,"Не все продукты доступны сейчас! 😔")

    elif language == "eng":
        if person[0] is not None:
            markup.add(KeyboardButton(text="📥 Basket"))
            markup.add(KeyboardButton(text="✅ I filled the basket"))
        son_ = 0
        if menu[3] is not None:
            waffle = menu[5].split('.')
            son = 0
            for i in waffle:
                i = i.split(',')
                if i[0] == "True":
                    son = 1
                    son_ = 1
            if son == 1:
                markup.add(KeyboardButton(text="🧇 Waffles"))

        if menu[3] is not None:
            drinks = menu[3].split('.')
            son = 0
            for i in drinks:
                i = i.split(',')
                if i[0] == "True":
                    son = 1
                    son_ = 1
            if son == 1:
                    markup.add(KeyboardButton(text="🧃 Cool drinks"))

        if menu[2] is not None:
            coffee = menu[2].split('.')
            son = 0
            for i in coffee:
                i = i.split(',')
                if i[0] == "True":
                    son = 1
                    son_ = 1
            if son == 1:
                markup.add(KeyboardButton(text="☕️ Coffee"))

        if menu[1] is not None:
            fast_food = menu[1].split('.')
            son = 0
            for i in fast_food:
                i = i.split(',')
                if i[0] == "True":
                    son = 1
                    son_ = 1
            if son == 1:
                markup.add(KeyboardButton(text="🍔️️ Fast Food"))

        if son_ == 1:
            if true == 1:
                await bot.send_message(message.from_user.id,"Where to start?",reply_markup=markup)
        else:
            await bot.send_message(message.from_user.id,"Now all the products are finished! 😔")