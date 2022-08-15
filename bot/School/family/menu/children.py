from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



async def family_children(message:types.Message,family_conn,student_conn,vote_cb):
    children = family_conn.execute("select student from CHILDREN where id = (?);",(message.from_user.id,)).fetchall()
    markup = InlineKeyboardMarkup(row_width=2,inline_keyboard=True)
    for i in children:
        student = student_conn.execute("select first_name, last_name from CONN where number = (?);",(i[0],)).fetchall()[0]
        markup.insert(InlineKeyboardButton(text=f"{student[0]} {student[1]}",callback_data=vote_cb.new(name="student",province="children",city=i[0],school="None",tur="None",clas="None",action="family")))
    markup.insert(InlineKeyboardButton(text="Bola qo'shish",callback_data=vote_cb.new(name="student",province="children",city="new",school="None",tur="None",clas="None",action="family")))
    await bot.send_message(message.from_user.id,"Sizning bolalaringiz",reply_markup=markup)


async def family_student_menu(message:types.Message,vote_cb,callback_query):
    markup = InlineKeyboardMarkup(row_width=2,inline_keyboard=True)
    markup.row(
        InlineKeyboardButton(text="🧑🏻‍🏫Ustozlari",callback_data=vote_cb.new(name="teachers",province="children",city=callback_query["city"],school="None",tur="None",clas="None",action="family")),
        InlineKeyboardButton(text="Sinf ro'yxati",callback_data=vote_cb.new(name="class arr",province="children",city=callback_query["city"],school="None",tur="None",clas="None",action="family")),
        InlineKeyboardButton(text="📆Davomati",callback_data=vote_cb.new(name="attend",province="children",city=callback_query["city"],school="None",tur="None",clas="None",action="family")),
        InlineKeyboardButton(text="❌O'chirish",callback_data=vote_cb.new(name="delete",province="children",city=callback_query["city"],school="None",tur="None",clas="None",action="family")),
    )
    await bot.send_message(message.from_user.id,"Bollangizni sozlamalari",reply_markup=markup)

