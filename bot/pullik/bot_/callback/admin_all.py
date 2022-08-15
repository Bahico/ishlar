from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def get_admin_all(message: types.Message, conn, vote_cb):
    admin = conn.execute("select id, branch, name, phone_number from ADMIN;").fetchall()
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
