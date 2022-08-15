from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def bot_del_spare(message:types.Message,conn,vote_cb,callback_query):
    """
    kiritgan mashinaning
    :param message:
    :param conn:
    :param vote_cb:
    :param callback_query:
    :return: extiyot qismlarini chiqarib beradi
    """
    car_ = callback_query["name"].split(",")
    spare = conn.execute(f"select spare_name, number from SPARE where id = (?) and tur = (?);",(callback_query["name"],callback_query["stage"])).fetchall()
    markup = InlineKeyboardMarkup(resize_keyboard=True)
    markup.row_width = 3
    for i in spare:
        markup.insert(InlineKeyboardButton(text=i[0],callback_data=vote_cb.new(stage="spare_arr", id="del_menu", name=i[1], number=callback_query["stage"], language=callback_query["language"],action="bot")))
    if callback_query["language"] == "uzb":
        markup.insert(InlineKeyboardButton(text="Hammasi❌",callback_data=vote_cb.new(stage="spare_arr", id="del_menu", name=str(callback_query["stage"])+","+str(callback_query["name"]), number="all", language=callback_query["language"],action="bot")))
        markup.insert(InlineKeyboardButton(text="⬅️Ortga",callback_data=vote_cb.new(stage="year", id="del_menu", name=callback_query["name"], number="", language=callback_query["language"],action="bot")))
        await bot.send_message(message.from_user.id,f"pass",reply_markup=markup)


async def bot_del_all_spare(message:types.Message,conn,callback_query):
    """

    :param message:
    :param conn:
    :param callback_query:
    :return:
    """
    delete = callback_query["name"].split(",")
    conn.execute("delete from SPARE where id = (?) and tur = (?);",(int(delete[1]),delete[0]))
    if callback_query["language"] == "uzb":
        await bot.send_message(message.from_user.id,"☑️O'chirildi")
    elif callback_query["language"] == "eng":
        await bot.send_message(message.from_user.id,"☑️Deleted")
    elif callback_query["language"] == "rus":
        await bot.send_message(message.from_user.id,"☑️Удалено")