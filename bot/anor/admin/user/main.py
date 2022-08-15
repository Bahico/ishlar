import aiogram.utils.callback_data
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def admin_user(message: types.CallbackQuery,
                     vote_cb: aiogram.utils.callback_data.CallbackData):
    markup = InlineKeyboardMarkup(row_width=2).row(
        InlineKeyboardButton(text="Ko'rish", callback_data=vote_cb.new(rol='admin', stage="user", stage1="pagination",
                                                                       tur=10)),
        InlineKeyboardButton(text="Qo'shish",
                             callback_data=vote_cb.new(rol='admin', stage="add user", stage1="add",
                                                       tur=""))
    )
    markup.add(
        InlineKeyboardButton(text="Excel file",
                             callback_data=vote_cb.new(rol='admin', stage="user", stage1="excel",
                                                       tur=""))
    )
    await bot.send_message(message.from_user.id, "O'quvchilar menusi", reply_markup=markup)
