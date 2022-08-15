from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def get_user_number(message: types.Message, conn, vote_cb):
    branch = conn.execute("select id, name from BRANCH;").fetchall()
    admin = conn.execute("select id, branch, name, phone_number from CLIENT;").fetchall()
    if len(branch) == 1:
        son = 0
        markup = InlineKeyboardMarkup()
        for i in admin:
            # if i[1] == branch[0][0]:
            son += 1
            markup.row(
                InlineKeyboardButton(text=i[2],
                                     callback_data=vote_cb.new(location="client", text="communication", branch=i[0],
                                                               language="uzb", action="bot_")),
                InlineKeyboardButton(text="O'chirish❌",
                                     callback_data=vote_cb.new(location="client", text="delete", branch=i[0],
                                                               language="uzb", action="bot_")),
                InlineKeyboardButton(text="📱Telefon raqami",
                                     callback_data=vote_cb.new(location="client", text="phone", branch=i[3],
                                                               language="uzb", action="bot_"))
            )
        await bot.send_message(message.from_user.id, f"Haridorlar soni: {str(son)}\n\nHaridorlar👇👇", reply_markup=markup)
    elif len(branch) >= 1:
        awa = ""
        markup = InlineKeyboardMarkup()
        for i in branch:
            markup.add(InlineKeyboardButton(text=i[1],
                                            callback_data=vote_cb.new(location="branch", text="selection", branch=i[0],
                                                                      language="client", action="bot_")))
        markup.add(InlineKeyboardButton(text="Hammasi",
                                        callback_data=vote_cb.new(location="branch", text="all", branch="None",
                                                                  language="client", action="bot_")))
        await bot.send_message(message.from_user.id, "Qaysi filial👇👇", reply_markup=markup)
