from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from config import TOKEN

# 'location', 'text', 'branch', 'language', 'action'
# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def get_number(message: types.Message, conn, language, branch, food_type, food):
    conn.execute("update CLIENT set bosqich = (?) where id = (?)",(6,message.from_user.id))
    person = conn.execute("select basket from CLIENT where id = (?);",(message.from_user.id,)).fetchall()
    food_ = conn.execute(f"select {food_type} from BRANCH where id = (?);",(int(branch),)).fetchall()
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(
        KeyboardButton(text="1"),
        KeyboardButton(text="2"),
        KeyboardButton(text="3"),
        KeyboardButton(text="4"),
        KeyboardButton(text="5"),
        KeyboardButton(text="6"),
        KeyboardButton(text="7"),
        KeyboardButton(text="8"),
        KeyboardButton(text="9"))
    person = list(person[0])
    if language == "uzb":
        if person[0] is not None:
            markup.add(KeyboardButton(text="📥 Savat"))
        markup.add(KeyboardButton(text="⬅️ Orqaga"))
        son = None
        food_ = food_[0][0].split('.')
        for i in food_:
            i = i.split(',')
            if i[1] == food:
                son = i
        photo = conn.execute("select photo from PHOTO where food_name = (?);",(son[1],)).fetchall()
        await bot.send_photo(message.from_user.id,photo[0][0],f"{son[1]}\n\nNarx:{son[2]}",reply_markup=markup)
    elif language == "rus":
        if person[0] is not None:
            markup.add(KeyboardButton(text="📥 Корзина"))
        markup.add(KeyboardButton(text="⬅️ Назад"))
        son = None
        food_ = food_[0][0].split('.')
        for i in food_:
            i = i.split(',')
            if i[1] == food:
                son = i
        photo = conn.execute("select photo from PHOTO where food_name = (?);",(son[1],)).fetchall()
        await bot.send_photo(message.from_user.id,photo[0][0],f"{son[1]}\n\nЦена:{son[2]}",reply_markup=markup)

    elif language == "eng":
        if person[0] is not None:
            markup.add(KeyboardButton(text="📥 Basket"))
        markup.add(KeyboardButton(text="⬅️ Back"))
        son = None
        food_ = food_[0][0].split('.')
        for i in food_:
            i = i.split(',')
            if i[1] == food:
                son = i
        photo = conn.execute("select photo from PHOTO where food_name = (?);",(son[1],)).fetchall()
        await bot.send_photo(message.from_user.id,photo[0][0],f"{son[1]}\n\nPrice:{son[2]}",reply_markup=markup)