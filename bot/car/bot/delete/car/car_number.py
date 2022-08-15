from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.delete.spare.spare_type import bot_del_type
from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def bot_del_number(message:types.Message,conn,vote_cb,callback_query,error=None):
    """
    Mashinani turini olib
    :param error:
    :param message:
    :param conn:
    :param vote_cb:
    :param callback_query:
    :return: u mashinaning bor modellarini chiqarib beradi
    """
    i_ = conn.execute("select corporation from I where id = (?);",(message.from_user.id,)).fetchall()[0]
    car = conn.execute("select number from CAR where corporation = (?) and name = (?);",(i_[0],callback_query["name"],)).fetchall()
    car_set = set()
    for i in car:
        car_set.add(i[0])
    markup = InlineKeyboardMarkup(resize_keyboard=True)
    markup.row_width = 3
    for i in car_set:
        print(i)
        if i is not None and i != "bypass":
            markup.insert(InlineKeyboardButton(text=i,callback_data=vote_cb.new(stage="number", id="del_menu", name=i, number="", language=callback_query["language"],action="bot")))
    if callback_query["language"] == "uzb":
        markup.row(
            InlineKeyboardButton(text="Hammasi❌",callback_data=vote_cb.new(stage="number", id="del_menu", name=i_, number="all", language=callback_query["language"],action="bot")),
            InlineKeyboardButton(text="⬅️Ortga",callback_data=vote_cb.new(stage="spare_del", id="main_menu", name="None", number="None", language=callback_query["language"],action="bot")))
        if error is None:
            markup.add(InlineKeyboardButton(text="↪️ Barcha rusumlarga",callback_data=vote_cb.new(stage="number", id="del_menu", name="bypass", number=callback_query["name"], language=callback_query["language"],action="bot")))
            await bot.send_message(message.from_user.id,f"{callback_query['name']} mashinasining nechinchi modelidagi extiyot qismni o'chrish kerak?",reply_markup=markup)
        else:
            await bot.send_message(message.from_user.id,"Hozirda \"↪️ Barcha rusumlarga\" extiyot qism yo'q",reply_markup=markup)
    conn.execute(f"update I set name = '{callback_query['name']}' where id = '{message.from_user.id}'")

async def bot_del_name_bypass(message:types.Message,conn,vote_cb,callback_query):
    i_ = conn.execute("select corporation from I_ where id = (?);",(message.from_user.id,)).fetchall()[0]
    car = conn.execute("select id from CAR where corporation = (?) and name = (?) and number = 'bypass';",(i_[0],callback_query["number"],)).fetchall()
    if car:
        callback_query["name"] = car[0][0]
        await bot_del_type(message, vote_cb, callback_query)
    else:
        callback_query["name"] = callback_query["name"]
        await bot_del_number(message, conn, vote_cb, callback_query,True)

async def bot_del_all_number(message:types.Message,conn,callback_query):
    """

    :param message:
    :param conn:
    :param callback_query:
    :return:
    """
    i_ = conn.execute("select corporation from I_ where id = (?);",(message.from_user.id,)).fetchall()[0]
    car = conn.execute("select id from CAR where corporation = (?) and name = (?);",(i_[0],callback_query["name"])).fetchall()
    for i in car:
        conn.execute("delete from SPARE where id = (?);",(i[0],))
        conn.execute("delete from BRANCH_SPARE where id = (?);",(i[0],))
        conn.execute("delete from CLIENT_ where spare = (?);",(i[0],))
        conn.execute("delete from ADMIN_ where spare = (?);",(i[0],))
    conn.execute("delete from CAR where corporation = (?) and name = (?);",(i_[0],callback_query["name"]))
    conn.execute("delete from CLIENT_ where corporation = (?) and name = (?);",(i_[0],callback_query["name"]))
    conn.execute("delete from ADMIN_ where corporation = (?) and name = (?);",(i_[0],callback_query["name"]))
    if callback_query["language"] == "uzb":
        await bot.send_message(message.from_user.id,"☑️O'chirildi")
    elif callback_query["language"] == "eng":
        await bot.send_message(message.from_user.id,"☑️Deleted")
    elif callback_query["language"] == "rus":
        await bot.send_message(message.from_user.id,"☑️Удалено")
