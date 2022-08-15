from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.delete.spare.spare_type import bot_del_type
from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def bot_del_car_name(message:types.Message,conn,vote_cb,callback_query,error=None):
    """
    O'chiriladigan extiyot qismning mashina turlari
    :param error:
    :param message:
    :param conn:
    :param vote_cb:
    :param callback_query:
    :return: car arr
    """
    car = conn.execute("select name from CAR where corporation = (?);",(callback_query["name"],)).fetchall()
    car_set = set()
    for i in car:
        car_set.add(i[0])
    markup = InlineKeyboardMarkup(resize_keyboard=True)
    markup.row_width = 3
    for i in car_set:
        if i is not None and i != "bypass":
            markup.insert(InlineKeyboardButton(text=i,callback_data=vote_cb.new(stage="name", id="del_menu", name=i, number="None", language=callback_query["language"],action="bot")))

    if callback_query["language"] == "uzb":
        markup.row(
            InlineKeyboardButton(text="Hammasi❌",callback_data=vote_cb.new(stage="name", id="del_menu", name=callback_query["name"], number="all", language=callback_query["language"],action="bot")),
            InlineKeyboardButton(text="⬅️Ortga",callback_data=vote_cb.new(stage="spare_del", id="main_menu", name="back", number="None", language=callback_query["language"],action="bot")))
        if error is None:
            markup.add(InlineKeyboardButton(text="↪️Barcha modellarga",callback_data=vote_cb.new(stage="name", id="del_menu", name="bypass", number=callback_query["name"], language=callback_query["language"],action="bot")))
            await bot.send_message(message.from_user.id,"Qaysi turdagi mashinaning extiyot qisimi kerak",reply_markup=markup)
        else:
            await bot.send_message(message.from_user.id,"Hozirda \"↪️Barcha modellarga\" extiyot qism yo'q",reply_markup=markup)
    elif callback_query["language"] == "rus":
        markup.row(
            InlineKeyboardButton(text="Hammasi❌",callback_data=vote_cb.new(stage="name", id="del_menu", name=callback_query["name"], number="all", language=callback_query["language"],action="bot")),
            InlineKeyboardButton(text="⬅️Ortga",callback_data=vote_cb.new(stage="spare_del", id="main_menu", name="back", number="None", language=callback_query["language"],action="bot")))
        await bot.send_message(message.from_user.id,"Qaysi turdagi mashinaning extiyot qisimi kerak",reply_markup=markup)
    elif callback_query["language"] == "eng":
        markup.row(
            InlineKeyboardButton(text="Hammasi❌",callback_data=vote_cb.new(stage="name", id="del_menu", name=callback_query["name"], number="all", language=callback_query["language"],action="bot")),
            InlineKeyboardButton(text="⬅️Ortga",callback_data=vote_cb.new(stage="spare_del", id="main_menu", name="back", number="None", language=callback_query["language"],action="bot")))
        await bot.send_message(message.from_user.id,"Qaysi turdagi mashinaning extiyot qisimi kerak",reply_markup=markup)
    i = conn.execute("select * from I where id = (?);",(message.from_user.id,)).fetchall()
    if i: conn.execute(f"update I set corporation = '{callback_query['name']}' where id = (?);",(message.from_user.id,))
    else: conn.execute("insert into I(id,corporation) values (?,?);",(message.from_user.id,callback_query["name"]))


async def bot_del_name_bypass(message:types.Message,conn,vote_cb,callback_query):
    car = conn.execute("select id from CAR where corporation = (?) and name = 'bypass';",(callback_query["number"],)).fetchall()
    if car:
        callback_query["name"] = car[0][0]
        await bot_del_type(message, vote_cb, callback_query)
    else:
        callback_query["name"] = callback_query["name"]
        await bot_del_car_name(message, conn, vote_cb, callback_query,True)


async def bot_del_all_name(message:types.Message,conn,callback_query):
    """
    Barcha mashinalarni o'chirib yuboradi
    :param message:
    :param conn:
    :param callback_query:
    :return: qayta mashina qo'shish menusini chiqarib beradi
    """
    car = conn.execute("select id from CAR where corporation = (?);",(callback_query["name"],)).fetchall()
    for i in car:
        conn.execute("delete from SPARE where id = (?);",(i[0],))
        conn.execute("delete from BRANCH_SPARE where id = (?);",(i[0],))
        conn.execute("delete from CLIENT_ where spare = (?);",(i[0],))
        conn.execute("delete from ADMIN_ where spare = (?);",(i[0],))
    conn.execute("delete from CAR where corporation = (?);",(callback_query["name"],))
    conn.execute("delete from CLIENT_ where corporation = (?);",(callback_query["name"],))
    conn.execute("delete from ADMIN_ where corporation = (?);",(callback_query["name"],))
    if callback_query["language"] == "uzb":
        await bot.send_message(message.from_user.id,"☑️O'chirildi")
    elif callback_query["language"] == "eng":
        await bot.send_message(message.from_user.id,"☑️Deleted")
    elif callback_query["language"] == "rus":
        await bot.send_message(message.from_user.id,"☑️Удалено")
