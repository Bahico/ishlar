import aiogram.utils.callback_data
from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def admin_settings_main(message: types.Message, vote_cb: aiogram.utils.callback_data.CallbackData,
                              callback_query: dict):
    markup = InlineKeyboardMarkup(resize_keyboard=True)
    if callback_query["language"] == "uzb":
        markup.row(
            InlineKeyboardButton(text="🇺🇿Tilni o'zgartirish",
                                 callback_data=vote_cb.new(stage="language", id="settings_menu", name="None",
                                                           number=callback_query["number"],
                                                           language=callback_query["language"], action="branch"))
        )
        markup.row(
            InlineKeyboardButton(text="Filial nomni o'zgartirish",
                                 callback_data=vote_cb.new(stage="edit_name", id="settings_menu", name="None",
                                                           number=callback_query["number"],
                                                           language=callback_query["language"], action="branch")),
            InlineKeyboardButton(text="Maxsulotlar",
                                 callback_data=vote_cb.new(stage="spare", id="settings_menu", name="None",
                                                           number=callback_query["number"],
                                                           language=callback_query["language"], action="branch"))
        )
        await bot.send_message(message.from_user.id, "Sozlamalar👇🏻👇🏻", reply_markup=markup)
