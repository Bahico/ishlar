from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def bot_branch_menu(message: types.Message, vote_cb, callback_query):
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    if callback_query["language"] == "uzb":
        markup.row(
            InlineKeyboardButton(text="Filial qo'shish",callback_data=vote_cb.new(stage="add", id="branch", name="None",number="None", language=callback_query["language"],action="bot")),
            InlineKeyboardButton(text="Filial o'chirish",callback_data=vote_cb.new(stage="del", id="branch", name="None",number="None", language=callback_query["language"],action="bot")),
            InlineKeyboardButton(text="Filiallarni ko'rish",callback_data=vote_cb.new(stage="arr", id="branch", name="None",number="None", language=callback_query["language"],action="bot"))
        )
        await bot.send_message(message.from_user.id, "Tanlang👇🏻👇🏻", reply_markup=markup)
    elif callback_query["language"] == "rus":
        markup.row(
            InlineKeyboardButton(text="Добавить ветку",callback_data=vote_cb.new(stage="add", id="branch", name="None",number="None", language=callback_query["language"],action="bot")),
            InlineKeyboardButton(text="Удаление ветки",callback_data=vote_cb.new(stage="del", id="branch", name="None",number="None", language=callback_query["language"],action="bot")),
            InlineKeyboardButton(text="Посмотреть ветки",callback_data=vote_cb.new(stage="arr", id="branch", name="None",number="None", language=callback_query["language"],action="bot"))
        )
        await bot.send_message(message.from_user.id, "Выбирать👇🏻👇🏻", reply_markup=markup)
    elif callback_query["language"] == "eng":
        markup.row(
            InlineKeyboardButton(text="Add a branch",callback_data=vote_cb.new(stage="add", id="branch", name="None",number="None", language=callback_query["language"],action="bot")),
            InlineKeyboardButton(text="Branch deletion",callback_data=vote_cb.new(stage="del", id="branch", name="None",number="None", language=callback_query["language"],action="bot")),
            InlineKeyboardButton(text="View branches",callback_data=vote_cb.new(stage="arr", id="branch", name="None",number="None", language=callback_query["language"],action="bot"))
        )
        await bot.send_message(message.from_user.id, "Select👇🏻👇🏻", reply_markup=markup)
