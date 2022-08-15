import datetime

import sqlite3

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from markup import PessangerMenu2, PessangerMenu, AdminMenu, NextMenu, backMenu


TOKEN = '2119888679:AAHoqMmB8gf8jPmNs4m8zb9bPel0i51E4ek'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

conn = sqlite3.connect('sqlite.db')


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    conchi = conn.execute("select * from COMPANY where ID = (?);", (str(message.chat.id),))
    i = list(conchi)
    if i == []:
        await bot.send_message(message.from_user.id, "Assalomu aleykum {0.first_name}\nTaksi kerakmi nomeringizni va turgan joyingizni kiriting\n\nEslatib o'tamiz bu bot Qo'rg'ontepa Atrofida ishlaydi".format(message.from_user),reply_markup=PessangerMenu)
        conn.execute("insert into COMPANY (ID) values (?);",(str(message.chat.id),))
    elif list(conchi)[4] == 'ADMIN':
        await bot.send_message(message.from_user.id, 'Assalomu aleykum {0.first_name}'.format(message.from_user),reply_markup=AdminMenu)

@dp.message_handler(content_types=['location'])
async def geo(message: types.Message):
    conn.execute(f"update COMPANY set LOCATIONLAN = {str(message.location.longitude)}, LOCATIONLNG = {str(message.location.latitude)} where ID = (?);",(str(message.chat.id),))
    await bot.send_message(message.from_user.id,'Iltimos kuting \n x daqiqadan so\'ng telefon bo\'ladi',reply_markup=NextMenu)


@dp.message_handler(content_types=['contact'])
async def geo(message: types.Message):
    conn.execute(f"update COMPANY set CONTACT = {str(message.contact.phone_number)} where ID = (?);",(str(message.from_user.id),))
    await bot.send_message(message.from_user.id, 'Turgan joyingizni kiriting',reply_markup=PessangerMenu2)




@dp.message_handler(commands='admin')
async def geo(message: types.Message):
    conn.execute("update COMPANY set ADMIN = True where ID = (?);",(str(message.chat.id),))
    await bot.send_message(message.from_user.id,'Password', reply_markup=backMenu)

@dp.message_handler(commands='1208')
async def calendar(message: types.Message):
    conchi = conn.execute("select * from COMPANY where ID = (?);",(str(message.chat.id),))
    conchi = list(conchi)
    conchi = list(conchi[0])
    if conchi[4] == True:
        await bot.send_message(message.from_user.id, 'ishladi qoyil', reply_markup=AdminMenu)
        admin = "ADMIN"
        conn.execute(f'update COMPANY set ADMIN = {admin} where ID = (?);',(str(message.chat.id),))


# @dp.message_handler(lambda date: True)
# async def cal(message: types.Message):
#     pass









@dp.message_handler()
async def echo_message(message: types.Message):
    if message.text == 'Taksi chaqirish':
        await bot.send_message(message.from_user.id, 'Raqamingizni kiriting',reply_markup=PessangerMenu)
    elif message.text == 'Telefon nomer':
        await bot.send_message(message.from_user.id, 'Raqamingizni kiriting',reply_markup=PessangerMenu2)
    elif message.text == 'Shu telelgram nomeri':
        await bot.send_message(message.from_user.id, 'Turgan joyingizni kiriting', reply_markup=PessangerMenu2)
    elif message.text == "O'zim nomer kiritaman":
        await bot.send_message(message.from_user.id, 'Turgan joyingizni kiriting', )
    elif message.text == "Orqaga":
        await bot.send_message(message.from_user.id, 'orqaga',reply_markup=NextMenu)
    # elif message.text == "Today":
    #     son = 0
    #     for i in date_array:
    #         son += 1
    #         await bot.send_message(message.from_user.id,i[0:])
    #     await bot.send_message(message.from_user.id, son)
    # elif message.text == "Date":
    #     date = True
    #     await bot.send_message(message.from_user.id,'Kunni kiriting')
    elif message.text == "Buyurtmalar":
        conchi = conn.execute("select * from COMPANY where ID = (?);",(str(message.chat.id),))
        conchi = list(conchi)
        i = list(conchi[0])
        if i[4] == 'ADMIN':
            cur = conn.execute("select * from COMPANY")
            cur = list(cur)
            print(cur)
            for i in cur:
                i = list(i)
                if i[2] != None:
                    print(True)
                    await bot.send_message(message.from_user.id, (i[1],i[2]))
                    conn.execute("update COMPANY set CONTACT = None, LOCATION = None where ID = (?);",(str(message.chat.id),))
    # if date:
    #     for table in date_table:
    #         if message.text == table[0]:
    #             son = 1
    #             for i in table:
    #                 son += 1
    #                 await bot.send_message(message.from_user.id, i)
    #             await bot.send_message(message.from_user.id, son)
    #             break












if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)