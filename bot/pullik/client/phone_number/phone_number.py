from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types

from client.delivery import branch
from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def get_phone(message: types.Message, conn, language):
    phone_number = message.text
    son = 0
    for i in phone_number:
        if son == 0:
            print(i)
            if i == "+":
                son = 1
            else:
                son = None
        else:
            if son is not None:
                try:
                    int(i)
                    son += 1
                except:
                    son = None
    if language == "uzb":
        if son is not None:
            if son == 13:
                conn.execute("update CLIENT set phone_number = (?) where id =(?);",
                             (phone_number[3:], message.from_user.id))
                await branch.get_branch_menu(message, conn, "uzb")
            else:
                await bot.send_message(message.from_user.id, "Iltimos raqamingizni +998 ********* shu ko'rinishida.")
        else:
            await bot.send_message(message.from_user.id, "Iltimos raqamingizni +998 ********* shu ko'rinishida.")
    elif language == "rus":
        if son is not None:
            if son == 13:
                conn.execute("update CLIENT set phone_number = (?) where id =(?);",
                             (phone_number[3:], message.from_user.id))
                await branch.get_branch_menu(message, conn, "uzb")
            else:
                await bot.send_message(message.from_user.id,
                                       "Пожалуйста, введите свой номер +998 ********** в этом представлении.")
        else:
            await bot.send_message(message.from_user.id,
                                   "Пожалуйста, введите свой номер +998 ********** в этом представлении.")
    elif language == "eng":
        if son is not None:
            if son == 13:
                conn.execute("update CLIENT set phone_number = (?) where id =(?);",
                             (phone_number[3:], message.from_user.id))
                await branch.get_branch_menu(message, conn, "uzb")
            else:
                await bot.send_message(message.from_user.id, "Please enter your number +998 ********* in this view.")
        else:
            await bot.send_message(message.from_user.id, "Please enter your number +998 ********* in this view.")
