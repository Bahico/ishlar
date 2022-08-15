from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def admin_branch_menu(message: types.Message, conn, vote_cb,language):
    conn.execute("update ADMIN set settings = '0' where id = (?);",(message.from_user.id,))
    if language == "uzb":
        markup = InlineKeyboardMarkup(resize_keyboard=True)
        markup.row(
            InlineKeyboardButton(text="🛒 Maxsulotlar",
                                 callback_data=vote_cb.new(stage="product", id="menu", name="None", number="branch",language=language, action="branch")),
            InlineKeyboardButton(text="⚙️ Filial sozlamalari",
                                 callback_data=vote_cb.new(stage="settings", id="menu", name="None", number="branch",language=language, action="branch"))
        )
        markup.row(
            InlineKeyboardButton(text="🙍🏻 Odamlar",
                                 callback_data=vote_cb.new(stage="people", id="menu", name="None", number="branch",language=language, action="branch")),
            InlineKeyboardButton(text="🗺 Filial joylashuvi",
                                 callback_data=vote_cb.new(stage="location", id="menu", name="None", number="branch",language=language, action="branch"))
        )
        markup.add(InlineKeyboardButton(text="🛢 Mashina yog'i",callback_data=vote_cb.new(stage="oil", id="menu", name="None", number="branch",language=language, action="branch")))
        await bot.send_message(message.from_user.id,"Bosh menu👇🏻👇🏻",reply_markup=markup)
    elif language == "eng":
        markup = InlineKeyboardMarkup(resize_keyboard=True)
        markup.row(
            InlineKeyboardButton(text="🛒 Products",
                                 callback_data=vote_cb.new(stage="product", id="menu", name="None", number="branch",language=language, action="branch")),
            InlineKeyboardButton(text="⚙️ Branch settings",
                                 callback_data=vote_cb.new(stage="settings", id="menu", name="None", number="branch",language=language, action="branch"))
        )
        markup.add(
            InlineKeyboardButton(text="🙍🏻 People",
                                 callback_data=vote_cb.new(stage="people", id="menu", name="None", number="branch",language=language, action="branch")),
            InlineKeyboardButton(text="🗺 Branch location",
                                 callback_data=vote_cb.new(stage="location", id="menu", name="None", number="branch",language=language, action="branch"))
        )
        markup.add(InlineKeyboardButton(text="🛢 Mashina yog'i",callback_data=vote_cb.new(stage="oil", id="menu", name="None", number="branch",language=language, action="branch")))
        await bot.send_message(message.from_user.id,"Main menu👇🏻👇🏻",reply_markup=markup)
    elif language == "rus":
        markup = InlineKeyboardMarkup(resize_keyboard=True)
        markup.row(
            InlineKeyboardButton(text="🛒 Продукты",
                                 callback_data=vote_cb.new(stage="product", id="menu", name="None", number="branch",language=language, action="branch")),
            InlineKeyboardButton(text="⚙️ Настройка филиала",
                                 callback_data=vote_cb.new(stage="settings", id="menu", name="None", number="branch",language=language, action="branch"))
        )
        markup.add(
            InlineKeyboardButton(text="🙍🏻 Люди",
                                 callback_data=vote_cb.new(stage="people", id="menu", name="None", number="branch",language=language, action="branch")),
            InlineKeyboardButton(text="🗺 Расположение филиала",
                                 callback_data=vote_cb.new(stage="location", id="menu", name="None", number="branch",language=language, action="branch"))
        )
        markup.add(InlineKeyboardButton(text="🛢 Mashina yog'i",callback_data=vote_cb.new(stage="oil", id="menu", name="None", number="branch",language=language, action="branch")))
        await bot.send_message(message.from_user.id,"Главное меню👇🏻👇🏻",reply_markup=markup)
