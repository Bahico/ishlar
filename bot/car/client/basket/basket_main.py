from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from client.car_arr.car_corporation import client_car_corporation
from config import TOKEN

# some code

# "id", "language", "action"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


# async def client_location(message:types.Message,conn,callback_query):
#     """
#     client location ini olish uchun so'rov yuboradi
#     :param message:
#     :param conn:
#     :param callback_query:
#     :return:
#     """
#     markup = ReplyKeyboardMarkup(resize_keyboard=True)
#     conn.execute("update CLIENT set settings = 'my_location' where id = (?);",(message.from_user.id,))
#     if callback_query["language"] == "uzb":
#         markup.add(KeyboardButton("🗺 Turgan joyim",request_location=True))
#         await bot.send_message(message.from_user.id,"Turgan joyingizni kiriting.",reply_markup=markup)
#     elif callback_query["language"] == "rus":
#         markup.add(KeyboardButton("🗺 Где я стою",request_location=True))
#         await bot.send_message(message.from_user.id,"Введите свое местоположение.",reply_markup=markup)
#     elif callback_query["language"] == "ENG":
#         markup.add(KeyboardButton("🗺 Location",request_location=True))
#         await bot.send_message(message.from_user.id,"Enter your location.",reply_markup=markup)




async def client_basket(message: types.Message, conn, vote_cb, callback_query):
    """
    Bu odam olaman degan qismlarni topadi qayerdanligini
    :param message:
    :param conn:
    :param vote_cb:
    :param callback_query:
    :return: topgan malumotlarni chiqarib beradi
    """

    basket = conn.execute("select basket from CLIENT_ where id = (?);",(message.from_user.id,)).fetchall()[0]
    markup = InlineKeyboardMarkup(reply_keybpard=True)
    awa = ""
    son = 0
    if basket[0] is not None:
        for spare_arr in basket[0].split("."):
            son += 1
            spare_arr = spare_arr.split(",")
            spare = conn.execute("select spare_name from SPARE where number = (?);",(int(spare_arr[1]),)).fetchall()[0]
            awa += str(son)+")"+spare[0]+" dan  1x"+spare_arr[0]+" ta\n\n"
            markup.row(
                InlineKeyboardButton(text=spare[0],callback_data=vote_cb.new(stage="info", id="spare_menu",name=son,number="", language=callback_query["language"],action="client")),
                InlineKeyboardButton(text="-",callback_data=vote_cb.new(stage="-", id="spare_menu",name=son,number="", language=callback_query["language"],action="client")),
                InlineKeyboardButton(text="+",callback_data=vote_cb.new(stage="+", id="spare_menu",name=son,number="", language=callback_query["language"],action="client")),
                InlineKeyboardButton(text="🗑",callback_data=vote_cb.new(stage="delete", id="spare_menu",name=son,number="", language=callback_query["language"],action="client")),
            )
        markup.row(
            InlineKeyboardButton(text="🗑 Hammasini tozalash",callback_data=vote_cb.new(stage="clear basket", id="spare_menu",name=son,number="", language=callback_query["language"],action="client")),
            InlineKeyboardButton(text="✅Sotib olish",callback_data=vote_cb.new(stage="buy", id="spare_menu",name=son,number="", language=callback_query["language"],action="client"))
        )
    else:
        await bot.send_message(message.from_user.id,"Hali hech nima yo'q")
        await client_car_corporation(message, conn, vote_cb, callback_query["language"])
    if basket is not None: await bot.send_message(message.from_user.id,awa,reply_markup=markup)



            