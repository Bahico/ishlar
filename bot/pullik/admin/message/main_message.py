from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

son = 4


async def get_message_admin(message: types.Message, conn):
    global son
    person = conn.execute("select bosqich, branch, settings, plus, minus from ADMIN where id = (?);",(message.from_user.id,)).fetchall()
    branch = conn.execute("select food_code, delivery_code, name, id from BRANCH;").fetchall()
    person = person[0]
    if person[0] == 1:
        if len(branch) == 1:
            if message.text == "Buyurtma qabul qilish":
                conn.execute("update ADMIN set settings = (?), branch = (?), bosqich = (?) where id = (?);",("delivery", branch[0][3], 2, message.from_user.id))
                await bot.send_message(message.from_user.id, "Password:",reply_markup=ReplyKeyboardRemove())
            elif message.text == "Ovqat kiritish":
                conn.execute("update ADMIN set settings = (?), branch = (?), bosqich = (?) where id = (?);",("food", branch[0][3], 2, message.from_user.id))
                await bot.send_message(message.from_user.id, "Password:",reply_markup=ReplyKeyboardRemove())
        elif not branch:
            await bot.send_message(message.from_user.id, "Hali Filial qo'shilmagan")
        else:
            for i in branch:
                if message.text == i[2]:
                    conn.execute("update ADMIN set branch = (?) where id = (?);", (i[3], message.from_user.id))
                    markup = ReplyKeyboardMarkup(resize_keyboard=True)
                    markup.add(KeyboardButton(text="Buyurtma qabul qilish"))
                    markup.add(KeyboardButton(text="Ovqat kiritish"))
                    await bot.send_message(message.from_user.id, "Tanlang👇👇", reply_markup=markup)
        if len(branch) != 1:
            if message.text == "Buyurtma qabul qilish":
                conn.execute("update ADMIN set settings = (?), bosqich = (?) where id = (?);", ("delivery", 2, message.from_user.id))
                markup = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("📱 Mening contactim",request_contact=True))
                await bot.send_message(message.from_user.id, "Password:",reply_markup=markup)
            elif message.text == "Ovqat kiritish":
                conn.execute("update ADMIN set settings = (?), bosqich = (?) where id = (?);", ("food", 2, message.from_user.id))
                markup = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("📱 Mening contactim",request_contact=True))
                await bot.send_message(message.from_user.id, "Contactingizni kiriting.",reply_markup=markup)
    elif person[0] == 2:
        if person[2] == "delivery":
            for i in branch:
                if i[3] == int(person[1]):
                    if son <= 1:
                        conn.execute("delete from ADMIN where id = (?);", (message.from_user.id,))
                        await bot.send_message(message.from_user.id, "No'tog'ri siz admin bo'lmaysiz")
                    else:
                        try:
                            if int(message.text) == i[1]:
                                conn.execute("update ADMIN set bosqich = (?) where id = (?);", (0, message.from_user.id))
                                await bot.send_message(message.from_user.id,
                                                       "Qabul qilindi!\n\nBotda ishlash uchun chatga 👉👉/menu deb yozing")
                                son = 4
                            else:
                                son -= 1
                                await bot.send_message(message.from_user.id,
                                                       f"Iltimos to'g'ri code kiriting\n\n{str(son)} imkoniyat qoldi")
                        except:
                            son -= 1
                            await bot.send_message(message.from_user.id,f"Iltimos to'g'ri code kiriting\n\n{str(son)} imkoniyat qoldi")
        if person[2] == "food":
            for i in branch:
                if i[3] == int(person[1]):
                    if son <= 1:
                        conn.execute("delete from ADMIN where id = (?);", (message.from_user.id,))
                        await bot.send_message(message.from_user.id, "No'tog'ri siz admin bo'lmaysiz")
                    else:
                        try:
                            if int(message.text) == i[0]:
                                conn.execute("update ADMIN set bosqich = (?) where id = (?);", (0, message.from_user.id))
                                await bot.send_message(message.from_user.id,
                                                       "Qabul qilindi!\n\nBotda ishlash uchun chatga 👉👉/menu deb yozing")
                                son = 4
                            else:
                                son -= 1
                                await bot.send_message(message.from_user.id,
                                                       f"Iltimos to'g'ri code kiriting\n\n{str(son)} imkoniyat qoldi")
                        except:
                            son -= 1
                            await bot.send_message(message.from_user.id,f"Iltimos to'g'ri code kiriting\n\n{str(son)} imkoniyat qoldi")
    elif person[0] == 3:
        conn.execute("update ADMIN set plus = (?), bosqich = (?) where id = (?);",(person[3]+","+message.text,4,message.from_user.id))
        await bot.send_message(message.from_user.id,"Maxsulotni narxini kiriting.\n\nIltimos narxda \". ,\" lar bolmasin")
    elif person[0] == 4:
        try:
            plus = person[3].split(',')
            plus = conn.execute(f"select {plus[0]} from BRANCH where id = (?);",(person[2],)).fetchall()
            int(message.text)
            if not plus:
                plus = person[3].split(",")
                conn.execute(f"update BRANCH set {plus[0]} = (?) where id = (?);",("True,"+plus[1]+","+message.text,person[1]))
            elif plus:
                conn.execute(f"update BRANCH set {plus[0]} = (?) where id = (?);",(plus[0][0]+"."+"True"+","+plus[1]+","+message.text,person[1]))
            conn.execute("update ADMIN set bosqich = 0 where id = (?);",(message.from_user.id,))
            await bot.send_message(message.from_user.id,"Endi maxsulotning rasmini kiriting")
        except:
            await bot.send_message(message.from_user.id,"Iltimos faqat son kiriting.")