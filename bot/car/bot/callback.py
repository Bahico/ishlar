from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from bot.branch.branch_add import get_branch_add_name
from bot.branch.branch_all_arr import bot_branch_all_arr
from bot.branch.branch_del import bot_branch_del, bot_yes_not, bot_yes_del
from bot.branch.menu import bot_branch_menu
from bot.code.code_edit import get_bot_code_edit
from bot.delete.car.car_brand import bot_del_brand, bot_del_all_brand
# from bot.delete.car.car_corporation import bot_car_corporation, bot_del_all_corporation
from bot.delete.car.car_name import bot_del_all_name, bot_del_car_name, bot_del_name_bypass
from bot.delete.car.car_number import bot_del_number, bot_del_all_number
from bot.delete.car.car_year import bot_del_year, bot_del_all_year
from bot.delete.spare.car_del import bot_car_del
from bot.delete.spare.spare_arr import bot_del_spare, bot_del_all_spare
from bot.delete.spare.spare_del import bot_del_del
from bot.delete.spare.spare_type import bot_del_type
from bot.delete.spare.yes_no import bot_del_true_false
from bot.language import bot_language
from bot.corporation import bot_corporation_add
from bot.menu.main_menu import bot_main_menu
from bot.people_number import get_people_number

from config import TOKEN

# some code

# "id", "language", "action"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def get_bot_callback(message: types.Message, conn, vote_cb, callback_query):
    if callback_query["id"] == "start":
        if callback_query["stage"] == "language":
            await bot_language(message, conn, vote_cb, callback_query)

    elif callback_query["id"] == "main_menu":
        if callback_query["stage"] == "branches":
            await bot_branch_menu(message, vote_cb, callback_query)
        elif callback_query["stage"] == "people":
            await get_people_number(message, conn, vote_cb, callback_query)
        elif callback_query["stage"] == "code_edit":
            await get_bot_code_edit(message, conn, callback_query)
        # elif callback_query["stage"] == "spare_del":
        #     await bot_car_corporation(message, conn, vote_cb, callback_query)
        elif callback_query["stage"] == "corporation add":
            await bot_corporation_add(message, conn, callback_query)

    elif callback_query["id"] == "branch":
        if callback_query["stage"] == "add":
            await get_branch_add_name(message, conn, callback_query)
        elif callback_query["stage"] == "del":
            await bot_branch_del(message, conn, vote_cb, callback_query)
        elif callback_query["stage"] == "arr":
            await bot_branch_all_arr(message, conn, vote_cb, callback_query)

        elif callback_query["stage"] == "delete":
            await bot_yes_not(message, vote_cb, callback_query)
        elif callback_query["stage"] == "yes":
            await bot_yes_del(message, vote_cb, conn, callback_query)
        elif callback_query["stage"] == "not":
            await bot_branch_menu(message, vote_cb, callback_query)

    elif callback_query["id"] == "del_menu":
        if callback_query["stage"] == "corporation":
            if callback_query["name"] == "all":
                pass
                # await bot_del_all_corporation(message, conn, vote_cb, callback_query)
            elif callback_query["name"] == "back":
                await bot_main_menu(message, vote_cb, callback_query["language"], conn)
            else:
                await bot_del_car_name(message, conn, vote_cb, callback_query)

        elif callback_query["stage"] == "name":
            if callback_query["number"] == "all":
                await bot_del_all_name(message, conn, callback_query)
            elif callback_query["name"] == "bypass":
                await bot_del_name_bypass(message, conn, vote_cb, callback_query)
            else:
                await bot_del_number(message, conn, vote_cb, callback_query)

        elif callback_query["stage"] == "number":
            if callback_query["number"] == "all":
                await bot_del_all_number(message, conn, callback_query)
            elif callback_query["name"] == "bypass":
                pass
            else:
                await bot_del_brand(message, conn, vote_cb, callback_query)

        elif callback_query["stage"] == "brand":
            if callback_query["number"] == "all":
                await bot_del_all_brand(message, conn, callback_query)
            elif callback_query["name"] == "bypass":
                pass
            else:
                await bot_del_year(message, conn, vote_cb, callback_query)

        elif callback_query["stage"] == "year":
            if callback_query["number"] == "all":
                await bot_del_all_year(message, conn, callback_query)
            elif callback_query["name"] == "bypass":
                pass
            else:
                await bot_del_type(message, vote_cb, callback_query)

        elif callback_query["stage"] == "kuzif":
            await bot_del_spare(message, conn, vote_cb, callback_query)
        elif callback_query["stage"] == "mator":
            await bot_del_spare(message, conn, vote_cb, callback_query)
        elif callback_query["stage"] == "tuning":
            await bot_del_spare(message, conn, vote_cb, callback_query)

        elif callback_query["stage"] == "spare_arr":
            if callback_query["number"] == "all":
                await bot_del_all_spare(message, conn, callback_query)
            else:
                await bot_del_true_false(message, vote_cb, callback_query)

        elif callback_query["stage"] == "all bypass":
            await bot_del_true_false(message, vote_cb, callback_query, True)

        elif callback_query["stage"] == "yes":
            if callback_query["number"] == "spare":
                await bot_del_del(message, conn, vote_cb, callback_query, 0)
            else:
                await bot_car_del(message, conn, vote_cb, callback_query)
        elif callback_query["stage"] == "not":
            await bot_del_del(message, conn, vote_cb, callback_query, 1)
    conn.commit()
