import sqlite3

from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove, ReplyKeyboardMarkup, \
    KeyboardButton
from aiogram.utils import executor
from aiogram.utils.callback_data import CallbackData

from client.start import start
from client.message.main_message import get_message_client, get_start
from client.main_menu.main_menu import get_menu_client
from client.callback.callback import get_callback_client
from client.client_location.location import get_client_location
from admin.start.start import get_start_admin
from admin.message.main_message import get_message_admin
from admin.menu.main_menu import get_admin_menu
from admin.callback.callback import get_admin_callback
from admin.update_photo.update_photo import get_photo
from bot_.add_branch.insert import get_insert_branch
from bot_.callback.callback import get_bot_callback

from config import TOKEN, code
from contact import get_contact

conn = sqlite3.connect('sqlite.db')

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

vote_cb = CallbackData('vote', 'location', 'text', 'branch', 'language', 'action')

branch_location_true = None
branch_delivery_code = None
branch_delivery_code_true = None
branch_food_code = None
branch_food_code_true = None
add_branch_name = None
main_code = code
My_code = code
I_Bot = None
snow = None


# 735095740
# DwichuzAdmin

@dp.message_handler(commands=['start'])
async def get_start_(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    await start.get_start(message)


@dp.message_handler(commands=['admin'])
async def get_admin(message: types.Message):
    await get_start_admin(message, conn)
    await bot.delete_message(message.from_user.id, message.message_id)


@dp.message_handler(commands=["logout"])
async def get_logout(message: types.Message):
    conn.execute("delete from CLIENT where id = (?);", (message.from_user.id,))
    conn.execute("delete from CLIENT where id = (?);", (message.from_user.id,))
    await bot.send_message(message.from_user.id, "O'chirlidingiz.✅")


@dp.message_handler(commands=['menu'])
async def get_menu(message: types.Message):
    global I_Bot
    if message.from_user.id == I_Bot:
        markup = InlineKeyboardMarkup(resize_keyboard=True)
        markup.add(
            InlineKeyboardButton(text="Filial qo'shish ➕",
                                 callback_data=vote_cb.new(location="branch", text="+", branch="None", language="uzb",
                                                           action="bot_")),
            InlineKeyboardButton(text="Filial o'chirish ➖",
                                 callback_data=vote_cb.new(location="branch", text="-", branch="None", language="uzb",
                                                           action="bot_"))
        )
        markup.row(
            InlineKeyboardButton(text="Adminar soni",
                                 callback_data=vote_cb.new(location="admin", text="number", branch="None",
                                                           language="uzb", action="bot_")),
            InlineKeyboardButton(text="Xaridorlar soni",
                                 callback_data=vote_cb.new(location="user", text="number", branch="None",
                                                           language="uzb", action="bot_"))
        )
        markup.row(
            InlineKeyboardButton(text="Kod o'zgartirish",
                                 callback_data=vote_cb.new(location="code", text="add", branch="None", language="uzb",
                                                           action="bot_"))
        )
        await bot.send_message(message.from_user.id, "Tanlang", reply_markup=markup)
    else:
        admin = conn.execute("select * from ADMIN where id = (?);", (message.from_user.id,)).fetchall()
        client = conn.execute("select language from CLIENT where id = (?);", (message.from_user.id,)).fetchall()
        if admin and not client:
            await get_admin_menu(message, conn, vote_cb)
        elif not admin and client:
            print(client[0][0])
            await get_menu_client(message, conn, client[0][0])
        else:
            await bot.send_message(message.from_user.id,
                                   "Iltimos chatga 👉👉/logout yozib keyin botdan foydalaning foydalaning!!!")
    await bot.delete_message(message.from_user.id, message.message_id)


@dp.callback_query_handler(vote_cb.filter(action="admin"))
async def get_admin(message: types.Message, callback_data: dict):
    await get_admin_callback(message, conn, vote_cb, callback_data)


@dp.callback_query_handler(vote_cb.filter(action="client"))
async def get_admin(message: types.Message, callback_data: dict):
    await get_callback_client(message, conn, callback_data, vote_cb)


@dp.callback_query_handler(vote_cb.filter(action="bot_"))
async def get_admin(message: types.Message, callback_data: dict):
    await get_bot_callback(message, conn, callback_data, vote_cb)


@dp.message_handler(content_types=['photo'])
async def get_message(message: types.Message):
    admin = conn.execute("select plus from ADMIN where id = (?);", (message.from_user.id,)).fetchall()
    if admin:
        if admin[0] is not None:
            await get_photo(message, conn, admin[0][0])
            await bot.send_photo(message.from_user.id, message.photo[0].file_id)
    else:
        await bot.send_message(message.from_user.id, "Siz admin emassiz")


@dp.message_handler(content_types=['location'])
async def get_location(message: types.Message):
    global I_Bot, branch_location_true
    if message.from_user.id == I_Bot and branch_location_true is True:
        await get_insert_branch(message, conn, branch_food_code, branch_delivery_code, add_branch_name)
        none()
    else:
        await get_client_location(message, conn)


@dp.message_handler(content_types=['contact'])
async def get_location(message: types.Message):
    await get_contact(message, conn)


@dp.message_handler(commands=['dwichuz'])
async def get_dwich(message: types.Message):
    global snow
    snow = message.from_user.id
    await bot.send_message(message.from_user.id, "Password:")


def none():
    global add_branch_name, branch_food_code_true, branch_food_code, branch_delivery_code_true, branch_delivery_code, branch_location_true
    delivery_edit = None
    food_edit = None
    communication = None
    branch_food_code_true = None
    branch_delivery_code_true = None
    branch_location_true = None


@dp.message_handler()
async def get_message(message: types.Message):
    global snow, My_code, I_Bot, add_branch_name, branch_food_code_true, branch_food_code, branch_delivery_code_true, branch_delivery_code, branch_location_true
    if message.from_user.id == snow:
        if message.text == str(My_code):
            I_Bot = message.from_user.id
            await bot.send_message(message.from_user.id, "Qabul qilindi.✅\n\nBot sizning qo'lingizda.")
            snow = None
    elif message.from_user.id == I_Bot:
        from bot_.add_branch.add_branch import add_branch_true, get_none
        from bot_.adit_code.branch import food_edit, delivery_edit, get_none_
        if add_branch_true is True:
            add_branch_name = message.text
            get_none()
            branch_food_code_true = True
            print("Qayta qayta")
            await bot.send_message(message.from_user.id,
                                   "Bu filialda maxsulotlarga javob beruvchi admin kodini kiriting.\n\nIltimos faqat sondan iborat bo'lsin.")
        elif branch_food_code_true is True:
            try:
                branch_food_code = int(message.text)
                get_none_()
                branch_food_code_true = None
                branch_delivery_code_true = True
                await bot.send_message(message.from_user.id, "Endi buyurtma qabul qilivchi admin kodini kiriting.")
            except:
                print("Xato")
                await bot.send_message(message.from_user.id,
                                       "Iltimos kod faqat sondan iborat bolsin\n\nXato: " + message.text)
        elif branch_delivery_code_true is True:
            try:
                branch_delivery_code = int(message.text)
                none()
                branch_location_true = True
                markup = ReplyKeyboardMarkup(resize_keyboard=True).add(
                    KeyboardButton("Location 🗺", request_location=True))
                await bot.send_message(message.from_user.id, "Filail qayerda joylashgan.", reply_markup=markup)
            except:
                await bot.send_message(message.from_user.id,
                                       "Iltimos kod faqat sondan iborat bo'lsin\n\nXato: " + message.text)
        elif delivery_edit is not None:
            try:
                conn.execute("update BRANCH set delivery_code = (?) where id = (?);",
                             (int(message.text), delivery_edit))
                get_none()
                await bot.send_message(message.from_user.id, "O'zgartirildi.✅\n\nO'zgartirilgan kod: " + message.text)
            except:
                await bot.send_message(message.from_user.id, "Iltimos faqat son kiriting")
        elif food_edit is not None:
            try:
                conn.execute("update BRANCH set food_code = (?) where id = (?);", (int(message.text), food_edit))
                get_none()
                await bot.send_message(message.from_user.id, "O'zgartirildi.✅\n\nO'zgartirilgan kod: " + message.text)
            except:
                await bot.send_message(message.from_user.id, "Iltimos faqat son kiriting")
    else:
        await get_start(message, conn)
        person = conn.execute("select * from CLIENT where id = (?);", (message.from_user.id,)).fetchall()
        admin = conn.execute("select * from ADMIN where id = (?);", (message.from_user.id,)).fetchall()
        if person:
            await get_message_client(message, conn, vote_cb)
        elif admin:
            await get_message_admin(message, conn)
    conn.commit()
    await bot.delete_message(message.from_user.id, message.message_id)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
