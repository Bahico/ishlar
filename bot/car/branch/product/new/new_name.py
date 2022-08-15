from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


# async def admin_new_corporation(message:types.Message, conn, vote_cb, callback_query):
#     """
#     Yangi zavot qoshish
#     :param message:
#     :param conn:
#     :param vote_cb:
#     :param callback_query:
#     :return:
#     """
#     conn.execute("update ADMIN set settings = 'add_corporation' where id = (?);",(message.from_user.id,))
#     markup = InlineKeyboardMarkup(resize_keyboard=True).row(
#         InlineKeyboardButton(text="STOP",callback_data=vote_cb.new(stage="stop", id="car_plus", name="None", number="None",language=language, action="branch"))
#     )
#     if callback_query["language"] == "uzb":
#         await bot.send_message(message.from_user.id,"Yangi mashina qo'shmoqchimisiz unda\n\nShu ko'rinishida kiriting: model,markasi,rusumi,pazitsiyasi,i.ch.y\n\nYoki adashgan bo'lsangiz \"STOP\" tugmasini bosing",reply_markup=markup)
#     elif callback_query["language"] == "rus":
#         await bot.send_message(message.from_user.id,"Если вы хотите добавить новый автомобиль, введите его следующим образом: модель,марка,модель,позиция,год изготовления\n\nИли \"СТОП\", если вы сбиваетесь с пути",reply_markup=markup)
#     elif callback_query["language"] == "eng":
#         await bot.send_message(message.from_user.id,"If you want to add a new car, enter it as follows: model,brand,model,position,year of manufacture\n\nOr \"STOP\" if you are go astray",reply_markup=markup)


async def admin_new_name(message: types.Message, conn, vote_cb, language):
    """
    Yangi mashina qo'shishga start beradi
    :param language:
    :param message:
    :param conn:
    :param vote_cb:
    :return:
    """
    print(language)
    conn.execute("update ADMIN set settings = 'add_name' where id = (?);", (message.from_user.id,)).fetchall()
    markup = InlineKeyboardMarkup(resize_keyboard=True).row(
        InlineKeyboardButton(text="STOP",callback_data=vote_cb.new(stage="stop", id="car_plus", name="None", number="None",language=language, action="branch"))
    )
    if language == "uzb":
        await bot.send_message(message.from_user.id,"Yangi mashinaning nomini kiriting \n\nYoki adashgan bo'lsangiz \"STOP\" tugmasini bosing",reply_markup=markup)
    elif language == "rus":
        await bot.send_message(message.from_user.id,"Если вы хотите добавить новый автомобиль, введите его следующим образом: марка,модель,позиция,год изготовления\n\nИли \"СТОП\", если вы сбиваетесь с пути",reply_markup=markup)
    elif language == "eng":
        await bot.send_message(message.from_user.id,"If you want to add a new car, enter it as follows: brand,model,position,year of manufacture\n\nOr \"STOP\" if you are go astray",reply_markup=markup)


async def admin_new_number(message: types.Message, conn, vote_cb, language, text=None):
    """
    Yangi model berishga start beradi
    :param text:
    :param language:
    :param message:
    :param conn:
    :param vote_cb:
    :return:
    """
    conn.execute("update ADMIN set settings = 'add_number' where id = (?);", (message.from_user.id,)).fetchall()
    if text: conn.execute(f"update ADMIN_ set name = '{message.text}' where id = (?);",(message.from_user.id,))
    markup = InlineKeyboardMarkup(resize_keyboard=True).row(
        InlineKeyboardButton(text="STOP",callback_data=vote_cb.new(stage="stop", id="car_plus", name="None", number="None",language=language, action="branch"))
    )
    if language == "uzb":
        await bot.send_message(message.from_user.id,f"Yangi mashinaning rusumini kiritng\n\nYoki adashgan bo'lsangiz \"STOP\" tugmasini bosing",reply_markup=markup)
    elif language == "rus":
        await bot.send_message(message.from_user.id,f"Добавить новую модель \n\nВведите так же: модель,пазиция,год изготовления\n\nИли нажмите кнопку «СТОП», если вы заблудились.",reply_markup=markup)
    elif language == "eng":
        await bot.send_message(message.from_user.id,f"To add a new model of  car\n\nEnter in this view: model,paditsiya,year of manufacture\n\nOr press the \"STOP\" button if you're going astray",reply_markup=markup)


async def admin_new_brand(message:types.Message,conn,vote_cb,language,text=None):
    """
    Yangi rusum qo'shishga start beradi
    :param text:
    :param message:
    :param conn:
    :param vote_cb:
    :param language: Lacetti 2
    :return:
    """
    conn.execute("update ADMIN set settings = 'add_brand' where id = (?);", (message.from_user.id,))
    if text: conn.execute(f"update ADMIN_ set number = '{message.text}' where id = (?);",(message.from_user.id,))
    markup = InlineKeyboardMarkup(resize_keyboard=True).row(
        InlineKeyboardButton(text="STOP",callback_data=vote_cb.new(stage="stop", id="car_plus", name="None", number="None",language=language, action="branch"))
    )
    if language == "uzb":
        await bot.send_message(message.from_user.id,f"Mashinasining yangi pazitsiyasini kiriting\n\nYoki adashgan bo'lsangiz \"STOP\" tugmasini bosing",reply_markup=markup)
    elif language == "rus":
        await bot.send_message(message.from_user.id,f"Введите новый бренд в этом представлении: пазиция,год изготовления\n\nИли нажмите кнопку \"STOP\", если вы заблудились.",reply_markup=markup)
    elif language == "eng":
        await bot.send_message(message.from_user.id,f"Enter the new version of in this view: model,year of manufacture\n\nOr press the \"STOP\" button if you're going astray",reply_markup=markup)


async def admin_new_year(message:types.Message,conn,vote_cb,language,text=None):
    conn.execute("update ADMIN set settings = 'add_year' where id = (?);", (message.from_user.id,))
    if text: conn.execute(f"update ADMIN_ set paditsiya = '{message.text}' where id = (?);",(message.from_user.id,))
    markup = InlineKeyboardMarkup(resize_keyboard=True).row(InlineKeyboardButton(text="STOP",callback_data=vote_cb.new(stage="stop", id="car_plus", name="None", number="None",language=language, action="branch")))
    if language == "uzb":
        await bot.send_message(message.from_user.id,f"Yangi mashinaning yilini kiritng\n\nYoki adashgan bo'lsangiz \"STOP\" tugmasini bosing",reply_markup=markup)
    elif language == "rus":
        await bot.send_message(message.from_user.id,f"Bступи в новый год на позицию машины \n\nИли нажмите кнопку \"STOP\", если вы заблудились.",reply_markup=markup)
    elif language == "eng":
        await bot.send_message(message.from_user.id,f"Enter the new year in the nd position of the  machine\n\nOr press the \"STOP\" button if you're going astray",reply_markup=markup)
