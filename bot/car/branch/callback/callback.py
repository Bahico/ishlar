from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
# from ..bypass.bypass import branch_name_bypass, branch_number_bypass, branch_paditsiya_bypass, branch_year_bypass
from ..menu.main_menu import admin_branch_menu
from ..oil.oil_add import branch_oil_menu, branch_oil_type, branch_oil_arr, branch_oil_button_add, branch_oil_button
from ..settings.location.location import admin_branch_location
from ..settings.spare_number.spare_arr import admin_spare_arr
from ..start.start import admin_login
from ..product.product import admin_product
from ..product.product_plus import admin_plus_name, admin_plus_number, admin_plus_brand, admin_plus_model, \
    admin_plus_year, admin_plus_corporation
from ..product.new.new_name import admin_new_name, admin_new_number, admin_new_brand, \
    admin_new_year  # , admin_new_corporation
from ..product.add import admin_add_callback, admin_button
from ..settings.settings_main import admin_settings_main
from ..settings.language.language import admin_adit_language, admin_language_edit
from ..settings.edit_name.edit_name import admin_edit_name

from config import TOKEN

# some code

# "stage", "id", "name", "number", "language", "action"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def admin_branch_callback(message: types.Message, conn, vote_cb, callback_query):
    if callback_query["id"] == "start":
        if callback_query["stage"] == "start":
            await admin_login(message, conn, callback_query["language"])

    elif callback_query["id"] == "menu":
        if callback_query["stage"] == "product":
            await admin_product(message, vote_cb, callback_query)
        elif callback_query["stage"] == "settings":
            await admin_settings_main(message, vote_cb, callback_query)
        elif callback_query["stage"] == "people":
            await bot.send_message(message.from_user.id, "Hali bu funksiya ishlamayapti")
        elif callback_query["stage"] == "location":
            await admin_branch_location(message, conn, callback_query)
        elif callback_query["stage"] == "oil":
            await branch_oil_menu(message, vote_cb, callback_query)

    elif callback_query["id"] == "product":
        if callback_query["stage"] == "+":
            await admin_plus_corporation(message, conn, vote_cb, callback_query["language"])
        elif callback_query["stage"] == "-":
            pass  # await admin_product_minus(message, vote_cb, callback_query)

    elif callback_query["id"] == "plus":
        if callback_query["stage"] == "start":
            await admin_plus_name(message, conn, vote_cb, callback_query)

        elif callback_query["stage"] == "name":
            if callback_query["name"] == "new":
                await admin_new_name(message, conn, vote_cb, callback_query["language"])
            elif callback_query["name"] == "bypass":
                pass
                # await branch_name_bypass(message, conn, vote_cb, callback_query)
            else:
                await admin_plus_number(message, conn, vote_cb, callback_query)

        elif callback_query["stage"] == "number":
            if callback_query["number"] == "new":
                await admin_new_number(message, conn, vote_cb, callback_query["language"])
            elif callback_query["name"] == "bypass":
                pass
                # await branch_number_bypass(message, conn, vote_cb, callback_query)
            else:
                await admin_plus_model(message, conn, vote_cb, callback_query)

        elif callback_query["stage"] == "model":
            if callback_query["number"] == "new":
                await admin_new_brand(message, conn, vote_cb, callback_query["language"])
            elif callback_query["name"] == "bypass":
                pass # await branch_paditsiya_bypass(message, conn, vote_cb, callback_query)
            else:
                await admin_plus_year(message, conn, vote_cb, callback_query)

        elif callback_query["stage"] == "year":
            if callback_query["number"] == "new":
                await admin_new_year(message, conn, vote_cb, callback_query["language"])
            elif callback_query["name"] == "bypass":
                pass # await branch_year_bypass(message, conn, vote_cb, callback_query)
            else:
                await admin_plus_brand(message, conn, vote_cb, callback_query)

        elif callback_query["stage"] == "kuzif":
            await admin_add_callback(message, conn, vote_cb, callback_query)
        elif callback_query["stage"] == "mator":
            await admin_add_callback(message, conn, vote_cb, callback_query)
        elif callback_query["stage"] == "tuning":
            await admin_add_callback(message, conn, vote_cb, callback_query)

    elif callback_query["id"] == "car_plus":
        if callback_query["stage"] == "stop":
            conn.execute("update ADMIN set settings = NULL where id = (?);", (message.from_user.id,))
            if callback_query["language"] == "uzb":
                await bot.send_message(message.from_user.id, "Iltimos botdan tog'ri foydalaning!")
                await admin_branch_menu(message, conn, vote_cb, callback_query["language"])
            elif callback_query["language"] == "rus":
                await bot.send_message(message.from_user.id, "Пожалуйста, используйте бота правильно!")
                await admin_branch_menu(message, conn, vote_cb, callback_query["language"])
            elif callback_query["language"] == "eng":
                await bot.send_message(message.from_user.id, "Please use the bot correctly!")
                await admin_branch_menu(message, conn, vote_cb, callback_query["language"])

    elif callback_query["id"] == "spare_+":
        await admin_button(message, conn, callback_query)

    elif callback_query["id"] == "minus":
        pass  # await admin_minus_number(message, conn, vote_cb, callback_query)

    elif callback_query["id"] == "settings_menu":
        if callback_query["stage"] == "admins":
            pass
        elif callback_query["stage"] == "language":
            await admin_adit_language(message, conn, vote_cb, callback_query)
        elif callback_query["stage"] == "edit_name":
            await admin_edit_name(message, conn, vote_cb, callback_query)
        elif callback_query["stage"] == "spare":
            await admin_spare_arr(message, conn, vote_cb, callback_query)

    elif callback_query["id"] == "edit_language":
        await admin_language_edit(message, conn, vote_cb, callback_query)
    elif callback_query["id"] == "oil":
        await bot.send_message(message.from_user.id, "Hali bu funksiya ishlamayapti!!!\n\n/menu")

    elif callback_query["id"] == "oil":
        if callback_query["stage"] == "+":
            await branch_oil_type(message, vote_cb, callback_query)
        elif callback_query["stage"] == "-":
            pass

        elif callback_query["stage"] == "type":
            await branch_oil_arr(message, conn, vote_cb, callback_query)
        elif callback_query["stage"] == "oil":
            if callback_query["name"] == "new":
                await branch_oil_button(message, conn, callback_query)
            else:
                await branch_oil_button_add(message, conn, vote_cb, callback_query)

    conn.commit()
