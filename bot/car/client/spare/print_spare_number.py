from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from ..car_arr.car_corporation import client_car_corporation

from config import TOKEN

# some code

# "stage", "id", "name", "number", "language", "action"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def client_print_spare_number(message: types.Message, conn, vote_cb, callback_query):
    """

    :param message:
    :param conn:
    :param vote_cb:
    :param callback_query:
    :return:
    """
    spare = conn.execute("select spare_name from SPARE where number = (?);",(callback_query["name"],)).fetchall()[0]
    spare_photo = conn.execute("select photo from PHOTO where id = (?) and type = 'spare';",(callback_query["name"],)).fetchall()
    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    for i in range(1, 11):
        markup.insert(InlineKeyboardButton(text=str(i), callback_data=vote_cb.new(stage=callback_query["stage"], id="spare_",name=callback_query["name"],number=str(i),language=callback_query["language"],action="client")))
    if callback_query["language"] == "uzb":
        if spare_photo:await bot.send_photo(message.from_user.id,spare_photo[0][0],f"Sizga {spare[0]} dan qancha kerakligini tanlang yoki kiriting.",reply_markup=markup)
        else:await bot.send_message(message.from_user.id,f"Sizga {spare[0]} dan qancha kerakligini tanlang yoki kiriting.",reply_markup=markup)
    elif callback_query["language"] == "rus":
        await bot.send_message(message.from_user.id,f"Выберите или введите необходимое количество из {spare[0]}.",reply_markup=markup)
    elif callback_query["language"] == "eng":
        await bot.send_message(message.from_user.id,f"Select or enter the required quantity from {spare[0]}.",reply_markup=markup)


async def client_spare_button_number(message: types.Message, conn, vote_cb, callback_query):
    """
    Maxsulot miqdori tugmalarda
    :param message:
    :param conn:
    :param vote_cb:
    :param callback_query:
    :return: Maxsulotni qancha miqdorda olishini saqlaydi
    """
    client = conn.execute("select basket, spare from CLIENT_ where id = (?);", (message.from_user.id,)).fetchall()[0]
    if client[0] is None:
        conn.execute(f"update CLIENT_ set basket = '{callback_query['number'] + ',' + callback_query['name']}' where id = (?);",(message.from_user.id,))
    else:
        conn.execute(f"update CLIENT_ set basket = '{client[0] + '.' + str(callback_query['number']) + ','+ callback_query['name']}' where id = (?);",(message.from_user.id,))

    if callback_query["language"] == "uzb":
        await bot.send_message(message.from_user.id, "Yana biror narsa kerakmi? 😊")
        await client_car_corporation(message, conn, vote_cb, callback_query["language"])
    elif callback_query["language"] == "rus":
        await bot.send_message(message.from_user.id, "Хотели бы вы что-нибудь еще? 😊")
        await client_car_corporation(message, conn, vote_cb, callback_query["language"])
    elif callback_query["language"] == "eng":
        await bot.send_message(message.from_user.id, "Would you like anything else? 😊")
        await client_car_corporation(message, conn, vote_cb, callback_query["language"])
    conn.execute("update CLIENT set settings = '0' where id = (?);",(message.from_user.id,))
