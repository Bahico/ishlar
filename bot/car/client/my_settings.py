from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

from client.car_arr.car_corporation import client_car_corporation
from config import TOKEN

# some code

# "id", "language", "action"


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



async def client_phone_number(message:types.Message,conn,callback_query):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    conn.execute("insert into CLIENT(id,language,settings) values (?,?,?);",(message.from_user.id,callback_query["language"],"my_number"))
    print(conn.execute("select * from CLIENT;").fetchall())
    if callback_query["language"] == "uzb":
        markup.add(KeyboardButton("📱 Telefon raqamim",request_contact=True))
        await bot.send_message(message.from_user.id,"Contactingizni kiriting!",reply_markup=markup)

async def client_location(message:types.Message,conn,vote_cb,language):
    conn.execute("update CLIENT set longitude = (?), latitude = (?), settings = NULL where id = (?);",(message.location.longitude,message.location.latitude,message.from_user.id))
    await message.answer("✅✅",reply_markup=ReplyKeyboardRemove())
    try:
        await bot.delete_message(message.from_user.id,message.message_id-1)
    except:
        pass
    await client_car_corporation(message,conn,vote_cb,language)