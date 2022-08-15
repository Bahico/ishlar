from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.menu.main_menu import bot_main_menu
from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def bot_branch_del(message: types.Message, conn, vote_cb, callback_query):
    markup = InlineKeyboardMarkup(reply_keyboard=True)
    markup.row_width = 2
    branch = conn.execute("select name, id from BRANCH;").fetchall()
    for i in branch:
        markup.insert(
            InlineKeyboardButton(text=i[0], callback_data=vote_cb.new(stage="delete", id="branch", name=i[0],number=i[1], language=callback_query["language"],action="bot")))

    if callback_query["language"] == "uzb":
        await bot.send_message(message.from_user.id, "Qaysi filialni o'chirish kerak?", reply_markup=markup)
    elif callback_query["language"] == "rus":
        await bot.send_message(message.from_user.id, "Какой филиал закрыть?", reply_markup=markup)
    elif callback_query["language"] == "eng":
        await bot.send_message(message.from_user.id, "Which branch should be closed?", reply_markup=markup)



async def bot_yes_not(message: types.Message, vote_cb, callback_query):
    markup = InlineKeyboardMarkup(reply_keyboard=True)
    if callback_query["language"] == "uzb":
        markup.row(
            InlineKeyboardButton(text="✅HA", callback_data=vote_cb.new(stage="yes", id="branch", name=callback_query["name"],number=callback_query["number"], language=callback_query["language"],action="bot")),
            InlineKeyboardButton(text="❌YO'Q", callback_data=vote_cb.new(stage="not", id="branch", name="not",number=callback_query["number"],language=callback_query["language"],action="bot"))
        )
        await bot.send_message(message.from_user.id,f"Rostan {callback_query['name']} filialini o'chirmoqchimisiz?",reply_markup=markup)
    elif callback_query["language"] == "rus":
        markup.row(
            InlineKeyboardButton(text="✅ДА", callback_data=vote_cb.new(stage="yes", id="branch", name=callback_query["name"],number=callback_query["number"], language=callback_query["language"],action="bot")),
            InlineKeyboardButton(text="❌НЕТ", callback_data=vote_cb.new(stage="not", id="branch", name="not",number=callback_query["number"],language=callback_query["language"],action="bot"))
        )
        await bot.send_message(message.from_user.id,f"Вы действительно хотите удалить ветку {callback_query ['name']}?",reply_markup=markup)
    elif callback_query["language"] == "eng":
        markup.row(
            InlineKeyboardButton(text="✅YES", callback_data=vote_cb.new(stage="yes", id="branch", name=callback_query["name"],number=callback_query["number"], language=callback_query["language"],action="bot")),
            InlineKeyboardButton(text="❌NO", callback_data=vote_cb.new(stage="not", id="branch", name="not",number=callback_query["number"],language=callback_query["language"],action="bot"))
        )
        await bot.send_message(message.from_user.id,f"Do you really want to delete the {callback_query ['name']} branch?",reply_markup=markup)


async def bot_yes_del(message: types.Message, vote_cb, conn, callback_query):
    conn.execute("delete from BRANCH where id = (?);",(callback_query["number"],))
    conn.execute("delete from ADMIN where branch = (?);",(callback_query["number"],))
    if callback_query["language"] == "uzb":
        await bot.send_message(message.from_user.id,f"{callback_query['name']} nomli filial o'chirildi!")
        await bot_main_menu(message,vote_cb,callback_query["language"],conn)
    elif callback_query["language"] == "eng":
        await bot.send_message(message.from_user.id,f"A branch named {callback_query ['name']} has been removed!")
        await bot_main_menu(message,vote_cb,callback_query["language"],conn)
    elif callback_query["language"] == "rus":
        await bot.send_message(message.from_user.id,f"Ветка с именем {callback_query ['name']} удалена!")
        await bot_main_menu(message,vote_cb,callback_query["language"],conn)
