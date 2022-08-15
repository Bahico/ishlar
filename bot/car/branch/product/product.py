from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def admin_product(message: types.Message,vote_cb, callback_query):
    markup = InlineKeyboardMarkup(resize_keyboard=True)
    if callback_query["language"] == "uzb":
        markup.row(
            InlineKeyboardButton(text="Maxsulot qo'shish +",
                                 callback_data=vote_cb.new(stage="+", id="product", name="None",number=callback_query["number"],language=callback_query["language"], action="branch")),
            InlineKeyboardButton(text="Maxsulot o'chirish -",
                                 callback_data=vote_cb.new(stage="-", id="product", name="None",number=callback_query["number"],language=callback_query["language"], action="branch"))
        )
        await bot.send_message(message.from_user.id, "Maxsulot qo'shasizmi yo o'chirasizmi👇👇", reply_markup=markup)
    elif callback_query["language"] == "rus":
        markup.row(
            InlineKeyboardButton(text="Добавить продукт +",
                                 callback_data=vote_cb.new(stage="+", id="product", name="None",number=callback_query["number"],language=callback_query["language"], action="branch")),
            InlineKeyboardButton(text="Удалить продукт -",
                                 callback_data=vote_cb.new(stage="-", id="product", name="None",number=callback_query["number"],language=callback_query["language"], action="branch"))
        )
        await bot.send_message(message.from_user.id, "Добавляете ли вы или удаляете продукт👇👇", reply_markup=markup)
    elif callback_query["language"] == "eng":
        markup.row(
            InlineKeyboardButton(text="Add product +",
                                 callback_data=vote_cb.new(stage="+", id="product", name="None",number=callback_query["number"],language=callback_query["language"], action="branch")),
            InlineKeyboardButton(text="Delete the product -",
                                 callback_data=vote_cb.new(stage="-", id="product", name="None",number=callback_query["number"],language=callback_query["language"], action="branch"))
        )
        await bot.send_message(message.from_user.id, "Whether you add or delete a product👇👇", reply_markup=markup)
