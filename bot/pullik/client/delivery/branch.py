from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from config import TOKEN

# 'location', 'text', 'branch', 'language', 'action'
# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def get_branch_menu(message: types.Message, conn, language):
    conn.execute("update CLIENT set bosqich = (?) where id = (?);",(3,message.from_user.id))
    branch = conn.execute("select name from BRANCH where open = (?);",("True",)).fetchall()
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    if language == "uzb":
        son = 0
        for i in branch:
            son += 1
            markup.add(KeyboardButton(text=i[0]))
        markup.add(KeyboardButton(text="⬅️ Ortga"))
        if son != 1 and son != 0:
            await bot.send_message(message.from_user.id,"Hozirda ishlayotgan filiallar.",reply_markup=markup)
        elif son == 0:
            await bot.send_message(message.from_user.id,"Afsuski hozirgi vaqtda barcha filiallarimiz yopiq. 😔")
        elif son == 1:
            await bot.send_message(message.from_user.id,"Bizda bitta filialimiz ishlamoqda.",reply_markup=markup)
    elif language == "rus":
        son = 0
        for i in branch:
            son += 1
            markup.add(KeyboardButton(text=i[0]))
        markup.add(KeyboardButton(text="⬅️ Назад"))
        if son != 1 and son != 0:
            await bot.send_message(message.from_user.id,"Действующие филиалы.",reply_markup=markup)
        elif son == 0:
            await bot.send_message(message.from_user.id,"К сожалению, все наши филиалы в настоящее время закрыты. 😔")
        elif son == 1:
            await bot.send_message(message.from_user.id,"Hali bu funksiya ishlamayapti")
    elif language == "eng":
        son = 0
        for i in branch:
            son += 1
            markup.add(KeyboardButton(text=i[0]))
        markup.add(KeyboardButton(text="⬅️ Back"))
        if son != 1 and son != 0:
            await bot.send_message(message.from_user.id,"Currently operating branches.",reply_markup=markup)
        elif son == 0:
            await bot.send_message(message.from_user.id,"Unfortunately, all our branches are currently closed. 😔")
        elif son == 1:
            await bot.send_message(message.from_user.id,"Hali bu funksiya ishlamayapti")
