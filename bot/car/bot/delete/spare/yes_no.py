from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def bot_del_true_false(message:types.Message,vote_cb,callback_query,son=None):
    """
    niyyati aniqmi yoki yo'q ligini so'raydi
    :param son:
    :param message:
    :param vote_cb:
    :param callback_query:
    :return: qaysi extiyot qismni o'chirayotganini to'liq ko'rsatib niyyati aniqmi yoki yo'qligini so'raydi
    """
    markup = InlineKeyboardMarkup(resize_keyboard=True)
    if son: son = "car"
    else: son = "spare"
    if callback_query["language"] == "uzb":
        markup.row(
            InlineKeyboardButton(text="✅HA",callback_data=vote_cb.new(stage="yes", id="del_menu", name=callback_query["name"], number=son, language=callback_query["language"],action="bot")),
            InlineKeyboardButton(text="❌YO'Q",callback_data=vote_cb.new(stage="not", id="del_menu", name=callback_query["name"], number="", language=callback_query["language"],action="bot"))
        )
        await bot.send_message(message.from_user.id,f"pass",reply_markup=markup)
    elif callback_query["language"] == "rus":
        markup.row(
            InlineKeyboardButton(text="✅ДА",callback_data=vote_cb.new(stage="yes", id="del_menu", name=callback_query["name"], number=son, language=callback_query["language"],action="bot")),
            InlineKeyboardButton(text="❌НЕТ",callback_data=vote_cb.new(stage="not", id="del_menu", name=callback_query["name"], number="", language=callback_query["language"],action="bot"))
        )
        await bot.send_message(message.from_user.id,f"pass",reply_markup=markup)
    elif callback_query["language"] == "eng":
        markup.row(
            InlineKeyboardButton(text="✅YES",callback_data=vote_cb.new(stage="yes", id="del_menu", name=callback_query["name"], number=son, language=callback_query["language"],action="bot")),
            InlineKeyboardButton(text="❌NO",callback_data=vote_cb.new(stage="not", id="del_menu", name=callback_query["name"], number="", language=callback_query["language"],action="bot"))
        )
        await bot.send_message(message.from_user.id,f"pass",reply_markup=markup)