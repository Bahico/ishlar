import aiogram.utils.callback_data
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def admin_menu(message: types.Message or types.CallbackQuery, vote_cb: aiogram.utils.callback_data.CallbackData):
    markup = InlineKeyboardMarkup().row(
        InlineKeyboardButton(text="📚Dars qo'shish",
                             callback_data=vote_cb.new(rol='admin', stage="lessen", stage1="add",
                                                       tur="")),
        InlineKeyboardButton(text="🗂Katigory yaratish",
                             callback_data=vote_cb.new(rol='admin', stage="category", stage1="add",
                                                       tur=""))
    )
    markup.add(
        InlineKeyboardButton(text="🔐Kodni yangilash",
                             callback_data=vote_cb.new(rol='admin', stage="code", stage1="edit",
                                                       tur=""))
    )
    markup.row(
        InlineKeyboardButton(text="👨‍🎓O'quvchilar",
                             callback_data=vote_cb.new(rol='admin', stage="user", stage1="user",
                                                       tur="")),
        InlineKeyboardButton(text="💵Tolov",
                             callback_data=vote_cb.new(rol='admin', stage="payment", stage1="payment",
                                                       tur=""))
    )
    await bot.send_message(message.from_user.id, "Admin menu", reply_markup=markup)
