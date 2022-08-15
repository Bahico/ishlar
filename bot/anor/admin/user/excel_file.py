import xlsxwriter
import sqlite3

import aiogram.utils.callback_data
from aiogram import Bot, Dispatcher, types

from admin.menu import admin_menu
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def admin_user_excel(message: types.CallbackQuery, main_conn: sqlite3.Connection,
                           vote_cb: aiogram.utils.callback_data.CallbackData):
    workbook = xlsxwriter.Workbook('hello.xlsx')
    worksheet = workbook.add_worksheet()
    students = main_conn.execute("select * from users;").fetchall()
    row = 0
    col = 0
    for number, id, username, phone_number in students:
        fan = main_conn.execute("select name, number from lessen_fan where id = (?);", (number,)).fetchall()[0]
        category = main_conn.execute("select name from lessen_category where id = (?);", (fan[1],)).fetchall()[0][0]
        worksheet.write(row, col, id)
        worksheet.write(row, col+1, category)
        worksheet.write(row, col+2, fan[0])
        worksheet.write(row, col + 3, username)
        if phone_number:
            worksheet.write(row, col + 4, phone_number)
        row += 1
    workbook.close()
    await bot.send_document(message.from_user.id, document=open("hello.xlsx", "rb"), thumb="document")
    await admin_menu(message, vote_cb)
