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
            InlineKeyboardButton(text="π Maxsulotlar",
                                 callback_data=vote_cb.new(stage="product", id="menu", name="None", number="branch",language=language, action="branch")),
            InlineKeyboardButton(text="βοΈ Filial sozlamalari",
                                 callback_data=vote_cb.new(stage="settings", id="menu", name="None", number="branch",language=language, action="branch"))
        )
        markup.row(
            InlineKeyboardButton(text="ππ» Odamlar",
                                 callback_data=vote_cb.new(stage="people", id="menu", name="None", number="branch",language=language, action="branch")),
            InlineKeyboardButton(text="πΊ Filial joylashuvi",
                                 callback_data=vote_cb.new(stage="location", id="menu", name="None", number="branch",language=language, action="branch"))
        )
        markup.add(InlineKeyboardButton(text="π’ Mashina yog'i",callback_data=vote_cb.new(stage="oil", id="menu", name="None", number="branch",language=language, action="branch")))
        await bot.send_message(message.from_user.id,"Bosh menuππ»ππ»",reply_markup=markup)
    elif language == "eng":
        markup = InlineKeyboardMarkup(resize_keyboard=True)
        markup.row(
            InlineKeyboardButton(text="π Products",
                                 callback_data=vote_cb.new(stage="product", id="menu", name="None", number="branch",language=language, action="branch")),
            InlineKeyboardButton(text="βοΈ Branch settings",
                                 callback_data=vote_cb.new(stage="settings", id="menu", name="None", number="branch",language=language, action="branch"))
        )
        markup.add(
            InlineKeyboardButton(text="ππ» People",
                                 callback_data=vote_cb.new(stage="people", id="menu", name="None", number="branch",language=language, action="branch")),
            InlineKeyboardButton(text="πΊ Branch location",
                                 callback_data=vote_cb.new(stage="location", id="menu", name="None", number="branch",language=language, action="branch"))
        )
        markup.add(InlineKeyboardButton(text="π’ Mashina yog'i",callback_data=vote_cb.new(stage="oil", id="menu", name="None", number="branch",language=language, action="branch")))
        await bot.send_message(message.from_user.id,"Main menuππ»ππ»",reply_markup=markup)
    elif language == "rus":
        markup = InlineKeyboardMarkup(resize_keyboard=True)
        markup.row(
            InlineKeyboardButton(text="π ΠΡΠΎΠ΄ΡΠΊΡΡ",
                                 callback_data=vote_cb.new(stage="product", id="menu", name="None", number="branch",language=language, action="branch")),
            InlineKeyboardButton(text="βοΈ ΠΠ°ΡΡΡΠΎΠΉΠΊΠ° ΡΠΈΠ»ΠΈΠ°Π»Π°",
                                 callback_data=vote_cb.new(stage="settings", id="menu", name="None", number="branch",language=language, action="branch"))
        )
        markup.add(
            InlineKeyboardButton(text="ππ» ΠΡΠ΄ΠΈ",
                                 callback_data=vote_cb.new(stage="people", id="menu", name="None", number="branch",language=language, action="branch")),
            InlineKeyboardButton(text="πΊ Π Π°ΡΠΏΠΎΠ»ΠΎΠΆΠ΅Π½ΠΈΠ΅ ΡΠΈΠ»ΠΈΠ°Π»Π°",
                                 callback_data=vote_cb.new(stage="location", id="menu", name="None", number="branch",language=language, action="branch"))
        )
        markup.add(InlineKeyboardButton(text="π’ Mashina yog'i",callback_data=vote_cb.new(stage="oil", id="menu", name="None", number="branch",language=language, action="branch")))
        await bot.send_message(message.from_user.id,"ΠΠ»Π°Π²Π½ΠΎΠ΅ ΠΌΠ΅Π½Ρππ»ππ»",reply_markup=markup)
