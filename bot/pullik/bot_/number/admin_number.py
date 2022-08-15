from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def get_admin_number(message: types.Message, conn, vote_cb):
    branch = conn.execute("select id, name from BRANCH;").fetchall()
    admin = conn.execute("select id, branch, name, phone_number from ADMIN;").fetchall()
    if len(branch) == 1:
        son = 0
        markup = InlineKeyboardMarkup()
        for i in admin:
            # if i[1] == branch[0][0]:
            son += 1
            markup.row(
                InlineKeyboardButton(text=i[2],
                                     callback_data=vote_cb.new(location="admin", text="communication", branch=i[0],
                                                               language="uzb", action="bot_")),
                InlineKeyboardButton(text="O'chirish❌",
                                     callback_data=vote_cb.new(location="admin", text="delete", branch=i[0],
                                                               language="uzb", action="bot_")),
                InlineKeyboardButton(text="📱Telefon raqami",
                                     callback_data=vote_cb.new(location="admin", text="phone", branch=i[3],
                                                               language="uzb", action="bot_"))
            )
        await bot.send_message(message.from_user.id, f"Adminlar soni: {str(son)}\n\nAdminlar👇👇", reply_markup=markup)
    elif len(branch) >= 1:
        awa = ""
        markup = InlineKeyboardMarkup()
        for i in branch:
            markup.add(InlineKeyboardButton(text=i[1], callback_data=vote_cb.new(location="branch",text="selection",branch=i[0],language="admin",action="bot_")))
        markup.add(InlineKeyboardButton(text="Hammasi",
                                        callback_data=vote_cb.new(location="branch", text="all", branch="None",
                                                                  language="admin", action="bot_")))
        await bot.send_message(message.from_user.id, "Qaysi filial👇👇", reply_markup=markup)
