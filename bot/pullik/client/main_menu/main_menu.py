from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from config import TOKEN

# 'location', 'text', 'branch', 'language', 'action'
# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def get_menu_client(message: types.Message, conn, language):
    person = conn.execute("select * from CLIENT where id = (?);",(message.from_user.id,)).fetchall()
    if not person:
        conn.execute("insert into CLIENT(id,language,bosqich) values (?,?,?);", (message.from_user.id, language,1))
    else:
        conn.execute("update CLIENT set bosqich = 1 where id = (?);",(message.from_user.id,))
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    if language == "uzb":
        markup.add(KeyboardButton(text="🍽 Menyu"))
        markup.add(KeyboardButton(text="📖 Buyurtmalar tarixi"))
        markup.add(KeyboardButton(text="✍️ Fikr bildirish"))
        markup.add(KeyboardButton(text="☎️ Biz bilan aloqa"))
        await bot.send_message(message.from_user.id, "Tanlang👇👇",reply_markup=markup)
    elif language == "rus":
        markup.add(KeyboardButton(text="🍽 Меню"))
        markup.add(KeyboardButton(text="📖 История заказов"))
        markup.add(KeyboardButton(text="✍️ Дать обратную связь"))
        markup.add(KeyboardButton(text="☎️ Связаться с нами"))
        await bot.send_message(message.from_user.id, "Выбирать👇👇",reply_markup=markup)
    elif language == "eng":
        markup.add(KeyboardButton(text="🍽 Menu"))
        markup.add(KeyboardButton(text="📖 Order history"))
        markup.add(KeyboardButton(text="✍️ Give feedback"))
        markup.add(KeyboardButton(text="☎️ Contact us"))
        await bot.send_message(message.from_user.id, "Select👇👇",reply_markup=markup)
