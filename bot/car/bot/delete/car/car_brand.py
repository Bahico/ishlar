from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.delete.spare.spare_type import bot_del_type
from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def bot_del_brand(message:types.Message,conn,vote_cb,callback_query,error=None):
    """
    Nomi nomeri ni oladi va shu turdagi mashinaning paditsiyalarini oladi
    :param error:
    :param message:
    :param conn:
    :param vote_cb:
    :param callback_query:
    :return: shu ro'yxatni chiqarib beradi
    """
    i = conn.execute("select corporation, name from I where id = (?);",(message.from_user.id,)).fetchall()[0]
    car = conn.execute("select paditsiya from CAR where corporation = (?) and name = (?) and number = (?);",(i[0],i[1],callback_query["name"])).fetchall()
    car_set = set()
    for i in car:
        car_set.add(i[0])
    markup = InlineKeyboardMarkup(resize_keyboard=True)
    markup.row_width = 3
    for i in car_set:
        if i is not None and i != "bypass":
            markup.insert(InlineKeyboardButton(text=i,callback_data=vote_cb.new(stage="brand", id="del_menu", name=callback_query["name"], number=i, language=callback_query["language"],action="bot")))
    if callback_query["language"] == "uzb":
        markup.row(
            InlineKeyboardButton(text="Hammasi❌",callback_data=vote_cb.new(stage="brand", id="del_menu", name=callback_query["name"], number="all", language=callback_query["language"],action="bot")),
            InlineKeyboardButton(text="⬅️Ortga",callback_data=vote_cb.new(stage="name", id="del_menu", name=callback_query["name"], number="None", language=callback_query["language"],action="bot")))
        if error is None:
            markup.add(InlineKeyboardButton(text="↪️ Barcha pazitsiyalar",callback_data=vote_cb.new(stage="brand", id="del_menu", name="bypass", number=callback_query["name"], language=callback_query["language"],action="bot")))
            await bot.send_message(message.from_user.id,f"Nechinchi pazitsiyani o'chirish kerak?",reply_markup=markup)
        else:
            await bot.send_message(message.from_user.id,"Hozirda \"↪️ Barcha pazitsiyalar\" ga maxsulot yo'q",reply_markup=markup)
    elif callback_query["language"] == "rus":
        markup.insert(InlineKeyboardButton(text="Hammasi❌",callback_data=vote_cb.new(stage="brand", id="del_menu", name=callback_query["name"], number="all", language=callback_query["language"],action="bot")))
        markup.insert(InlineKeyboardButton(text="⬅️Ortga",callback_data=vote_cb.new(stage="name", id="del_menu", name=callback_query["name"], number="None", language=callback_query["language"],action="bot")))
        await bot.send_message(message.from_user.id,f"{callback_query['name']} {str(callback_query['number'])} ning nechinchi paditsiyasidagi extiyot qisimini o'chirish kerak?",reply_markup=markup)
    elif callback_query["language"] == "eng":
        markup.insert(InlineKeyboardButton(text="Hammasi❌",callback_data=vote_cb.new(stage="brand", id="del_menu", name=callback_query["name"], number="all", language=callback_query["language"],action="bot")))
        markup.insert(InlineKeyboardButton(text="⬅️Ortga",callback_data=vote_cb.new(stage="name", id="del_menu", name=callback_query["name"], number="None", language=callback_query["language"],action="bot")))
        await bot.send_message(message.from_user.id,f"{callback_query['name']} {str(callback_query['number'])} ning nechinchi paditsiyasidagi extiyot qisimini o'chirish kerak?",reply_markup=markup)
    conn.execute(f"update I set number = '{callback_query['name']}' where id = '{message.from_user.id}'")


async def bot_del_name_bypass(message:types.Message,conn,vote_cb,callback_query):
    i_ = conn.execute("select corporation, name from I_ where id = (?);",(message.from_user.id,)).fetchall()[0]
    car = conn.execute("select id from CAR where corporation = (?) and name = (?) and number = (?) and paditsiya = 'bypass';",(i_[0],i_[1],callback_query["number"],)).fetchall()
    if car:
        callback_query["name"] = car[0][0]
        await bot_del_type(message, vote_cb, callback_query)
    else:
        callback_query["name"] = callback_query["name"]
        await bot_del_brand(message, conn, vote_cb, callback_query,True)



async def bot_del_all_brand(message:types.Message,conn,callback_query):
    """

    :param message:
    :param conn:
    :param callback_query:
    :return:
    """
    i_ = conn.execute("select corporation, name from I_ where id = (?);",(message.from_user.id,)).fetchall()[0]
    car = conn.execute("select id from CAR where corporation = (?) and name = (?) and number = (?);",(i_[0],i_[1],callback_query["name"])).fetchall()
    for i in car:
        conn.execute("delete from SPARE where id = (?);",(i[0],))
        conn.execute("delete from BRANCH_SPARE where id = (?);",(i[0],))
        conn.execute("delete from CLIENT_ where spare = (?);",(i[0],))
        conn.execute("delete from ADMIN_ where spare = (?);",(i[0],))
    conn.execute("delete from CLIENT_ where corporation = (?) and name = (?) and number = (?);",(i_[0],i_[1],callback_query["name"]))
    conn.execute("delete from ADMIN_ where corporation = (?) and name = (?) and number = (?);",(i_[0],i_[1],callback_query["name"]))
    conn.execute("delete from CAR where corporation = (?) and name = (?) and number = (?);",(i_[0],i_[1],callback_query["name"]))
    if callback_query["language"] == "uzb":
        await bot.send_message(message.from_user.id,"☑️O'chirildi")
    elif callback_query["language"] == "eng":
        await bot.send_message(message.from_user.id,"☑️Deleted")
    elif callback_query["language"] == "rus":
        await bot.send_message(message.from_user.id,"☑️Удалено")