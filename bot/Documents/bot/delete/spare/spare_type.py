import aiogram.utils.callback_data
from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def bot_del_type(message: types.Message, vote_cb: aiogram.utils.callback_data.CallbackData, callback_query: dict):
    """
   qaysi turdagi maxsulotni o'chirish keraklgini sorovchi funksiya
    :param message:
    :param vote_cb:
    :param callback_query:
    :return: 3 xil variant chiqarib beradi
    """
    markup = InlineKeyboardMarkup(resize_keyboard=True)
    if callback_query["language"] == "uzb":
        markup.row(
            InlineKeyboardButton(text="⚒ Kuzif",
                                 callback_data=vote_cb.new(stage="kuzif", id="del_menu", name=callback_query["name"],
                                                           number="", language=callback_query["language"],
                                                           action="bot")),
            InlineKeyboardButton(text="⚙️ Mator",
                                 callback_data=vote_cb.new(stage="mator", id="del_menu", name=callback_query["name"],
                                                           number="", language=callback_query["language"],
                                                           action="bot")),
            InlineKeyboardButton(text="💈 Tuning",
                                 callback_data=vote_cb.new(stage="tuning", id="del_menu", name=callback_query["name"],
                                                           number="", language=callback_query["language"],
                                                           action="bot"))
        )
        markup.row(
            InlineKeyboardButton(text="❌Kerak emas",
                                 callback_data=vote_cb.new(stage="0", id="del_menu", name=callback_query["name"],
                                                           number="", language=callback_query["language"],
                                                           action="bot")),
            InlineKeyboardButton(text="⬅️Ortga",
                                 callback_data=vote_cb.new(stage="brand", id="del_menu", name=callback_query["number"],
                                                           number="", language=callback_query["language"],
                                                           action="bot")))
        markup.add(InlineKeyboardButton(text="❌Hammasi", callback_data=vote_cb.new(stage="all bypass", id="del_menu",
                                                                                   name=callback_query["name"],
                                                                                   number="",
                                                                                   language=callback_query["language"],
                                                                                   action="bot")))
        await bot.send_message(message.from_user.id, "Qaysi turdagi extiyot qismni o'chirmoqchisiz?",
                               reply_markup=markup)
