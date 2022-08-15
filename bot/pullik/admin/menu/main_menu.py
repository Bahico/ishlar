from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

# 'location', 'text', 'branch', 'language', 'action'
# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def get_admin_menu(message: types.Message, conn, vote_cb):
    admin = conn.execute("select settings, bosqich, branch from ADMIN where id = (?);",
                         (message.from_user.id,)).fetchall()
    admin = admin[0]
    if admin[0] == "food":
        if int(admin[1]) == 0:
            markup = InlineKeyboardMarkup(resize_keyboard=True)
            markup.add(InlineKeyboardButton(text="Mahsulot kiritish",
                                            callback_data=vote_cb.new(location='+', text='menu', branch=admin[2],
                                                                      language="uzb", action="admin")))
            markup.add(InlineKeyboardButton(text="Mahsulotni o'chirish",
                                            callback_data=vote_cb.new(location='-', text='menu', branch=admin[2],
                                                                      language="uzb", action="admin")))
            markup.add(InlineKeyboardButton(text="Vaqtinchalik bor yo'q qilish",
                                            callback_data=vote_cb.new(location='--', text='menu', branch=admin[2],
                                                                      language="uzb", action="admin")))
            await bot.send_message(message.from_user.id, "Tanlang👇👇", reply_markup=markup)
