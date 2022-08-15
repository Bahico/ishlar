from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def admin_plus_corporation(message: types.Message, conn, vote_cb, language):
    car = conn.execute("select name, id from brand;").fetchall()
    markup = InlineKeyboardMarkup(resize_keyboard=True)
    markup.row_width = 3
    for i in car:
        markup.insert(InlineKeyboardButton(text=i[0],callback_data=vote_cb.new(stage="start",id='plus',name=i[1],number="",language=language,action="branch")))
    if language == "uzb":
        # markup.insert(InlineKeyboardButton(text="🚗Yangi",callback_data=vote_cb.new(stage="start", id="plus", name="new",number="None", language=language,action="branch")))
        await bot.send_message(message.from_user.id, "Qaysi markadagi mashinani extiyot qisimi qo'shiladi🙃\n\nYoki yangi mashina qo'shiladimi🤨", reply_markup=markup)
    elif language == "rus":
        # markup.insert(InlineKeyboardButton(text="🚗новый",callback_data=vote_cb.new(stage="start", id="plus", name="new",number="None", language=language,action="branch")))
        await bot.send_message(message.from_user.id, "Какие марки автозапчастей будут добавлены🙃\n\n Или будет ли добавлен новый автомобиль 🤨", reply_markup=markup)
    elif language == "eng":
        # markup.insert(InlineKeyboardButton(text="🚗New",callback_data=vote_cb.new(stage="start", id="plus", name="new", number="None", language=language, action="branch")))
        await bot.send_message(message.from_user.id, "What brands of auto parts will be added🙃\n\n Or whether a new car will be added 🤨", reply_markup=markup)


async def admin_plus_name(message: types.Message, conn, vote_cb, callback_query):
    car = conn.execute("select name from car where corporation = (?);",(callback_query["name"],)).fetchall()
    car_set = set()
    for i in car:
        car_set.add(i[0])
    markup = InlineKeyboardMarkup(resize_keyboard=True)
    markup.row_width = 3
    for i in car_set:
        if i != "bypass": markup.insert(InlineKeyboardButton(text=i,callback_data=vote_cb.new(stage="name", id="plus", name=i, number="None",language=callback_query["language"], action="branch")))
    markup.add(InlineKeyboardButton(text="Barcha modellarga ↪️",callback_data=vote_cb.new(stage="name", id="plus", name="bypass", number="", language=callback_query["language"], action="branch")))
    if callback_query["language"] == "uzb":
        markup.insert(InlineKeyboardButton(text="🚗Yangi",callback_data=vote_cb.new(stage="name", id="plus", name="new",number="None", language=callback_query["language"],action="branch")))
        await bot.send_message(message.from_user.id, "Qaysi turdagi mashinani extiyot qisimi qo'shiladi🙃\n\nYoki yangi mashina qo'shiladimi🤨", reply_markup=markup)
    elif callback_query["language"] == "rus":
        markup.insert(InlineKeyboardButton(text="🚗новый",callback_data=vote_cb.new(stage="start", id="plus", name="new",number="None", language=callback_query["language"],action="branch")))
        await bot.send_message(message.from_user.id, "Какой тип автозапчастей будет добавлен 🙃\n\n Или будет ли добавлен новый автомобиль 🤨", reply_markup=markup)
    elif callback_query["language"] == "eng":
        markup.insert(InlineKeyboardButton(text="🚗New",callback_data=vote_cb.new(stage="start", id="plus", name="new", number="None", language=callback_query["language"], action="branch")))
        await bot.send_message(message.from_user.id, "Which type of car spare part will be added 🙃\n\n Or whether a new car will be added 🤨", reply_markup=markup)
    admin = conn.execute("select * from admin_ where id = (?);",(message.from_user.id,)).fetchall()
    if admin:conn.execute(f"update ADMIN_ set corporation = '{callback_query['name']}' where id = (?);",(message.from_user.id,))
    else:conn.execute("insert into ADMIN_ (id,corporation) values (?,?);",(message.from_user.id,callback_query["name"]))

async def admin_plus_number(message: types.Message, conn, vote_cb, callback_query):
    admin = conn.execute("select corporation from ADMIN_ where id = (?);",(message.from_user.id,)).fetchall()[0][0]
    car = conn.execute(f"select number from CAR where corporation = {admin} and name = '{callback_query['name']}';").fetchall()
    car_set = set()
    for i in car:
        car_set.add(i[0])
    markup = InlineKeyboardMarkup(resize_keyboard=True)
    for i in car_set:
        if i != "bypass" and i is not None: markup.add(InlineKeyboardButton(text=i, callback_data=vote_cb.new(stage="number", id="plus", name=i, number="", language=callback_query["language"], action="branch")))
    markup.add(InlineKeyboardButton(text="Barcha rusumlarga ↪️",callback_data=vote_cb.new(stage="number", id="plus", name="bypass", number="", language=callback_query["language"], action="branch")))
    if callback_query["language"] == "uzb":
        markup.insert(InlineKeyboardButton(text="Yangi model", callback_data=vote_cb.new(stage="number", id="plus", name=callback_query["name"], number="new", language=callback_query["language"], action="branch")))
        await bot.send_message(message.from_user.id,f"{callback_query['name']} ning qaysi modelini extiyot qisimini qo'shish kerak?",reply_markup=markup)
    elif callback_query["language"] == "rus":
        markup.insert(InlineKeyboardButton(text="Новая модель", callback_data=vote_cb.new(stage="number", id="plus", name=callback_query["name"], number="new", language=callback_query["language"], action="branch")))
        await bot.send_message(message.from_user.id, f"К какой модели {callback_query['name']} добавить запчасть?",reply_markup=markup)
    elif callback_query["language"] == "eng":
        markup.insert(InlineKeyboardButton(text="New model", callback_data=vote_cb.new(stage="number", id="plus", name=callback_query["name"], number="new", language=callback_query["language"], action="branch")))
        await bot.send_message(message.from_user.id,f"To which {callback_query['name']} model should I add a spare part?",reply_markup=markup)
    conn.execute("update ADMIN_ set name = (?) where id = (?);",(callback_query["name"],message.from_user.id))


async def admin_plus_model(message: types.Message, conn, vote_cb, callback_query):
    admin = conn.execute("select corporation, name from ADMIN_ where id = (?);",(message.from_user.id,)).fetchall()[0]
    car = conn.execute(f"select paditsiya from CAR where corporation = {admin[0]} and name = '{admin[1]}' and number = '{callback_query['name']}';").fetchall()
    car_set = set()
    for i in car:
        car_set.add(i[0])
    markup = InlineKeyboardMarkup(resize_keyboard=True)
    markup.row_width = 3
    for i in car_set:
        if i != "bypass" and i is not None: markup.insert(InlineKeyboardButton(text=i,callback_data=vote_cb.new(stage="model", id="plus", name=i, number="", language=callback_query["language"], action="branch")))
    markup.add(InlineKeyboardButton(text="Barcha pazitsiyalarga ↪️",callback_data=vote_cb.new(stage="model", id="plus", name="bypass", number="", language=callback_query["language"], action="branch")))
    if callback_query["language"] == "uzb":
        markup.add(InlineKeyboardButton(text="Yangi pazitsiya",callback_data=vote_cb.new(stage="model", id="plus", name="", number="new", language=callback_query["language"], action="branch")))
        await bot.send_message(message.from_user.id,f"{callback_query['name']} {callback_query['number']} mashinasining qaysi pazitsiyasiga extiyot qism qo'shish kerak?.😉\n\nYoki yangi model qo'shamizmi?🤨",reply_markup=markup)
    elif callback_query["language"] == "rus":
        markup.add(InlineKeyboardButton(text="Новая позиция",callback_data=vote_cb.new(stage="model", id="plus", name="", number="new", language=callback_query["language"], action="branch")))
        await bot.send_message(message.from_user.id,f"На какую машину {callback_query['name']} {callback_query['number']} добавить запасную 😉\n\nИли нам добавить новую модель?🤨",reply_markup=markup)
    elif callback_query["language"] == "eng":
        markup.add(InlineKeyboardButton(text="New position",callback_data=vote_cb.new(stage="model", id="plus", name="", number="new", language=callback_query["language"], action="branch")))
        await bot.send_message(message.from_user.id,f"Which {callback_query['name']} {callback_query['number']} car needs a spare part added to it.😉\n\n Or do we add a new model?🤨",reply_markup=markup)
    conn.execute("update ADMIN_ set number = (?) where id = (?);",(callback_query["name"],message.from_user.id))


async def admin_plus_year(message: types.Message, conn, vote_cb, callback_query):
    admin = conn.execute("select corporation, name, number from ADMIN_ where id = (?);",(message.from_user.id,)).fetchall()[0]
    car = conn.execute(f"select year, id from CAR where corporation = {admin[0]} and name = '{admin[1]}' and number = '{admin[2]}' and paditsiya = '{callback_query['name']}';").fetchall()
    markup = InlineKeyboardMarkup(resize_keyboard=True)
    markup.row_width = 3
    for i in car:
        if i != "bypass" and i is not None: markup.add(InlineKeyboardButton(text=i[0], callback_data=vote_cb.new(stage="year", id="plus", name=i[1], number="", language=callback_query["language"], action="branch")))
    markup.add(InlineKeyboardButton(text="Barcha yillarga ↪️",callback_data=vote_cb.new(stage="number", id="plus", name="bypass", number="", language=callback_query["language"], action="branch")))
    if callback_query["language"] == "uzb":
        markup.add(InlineKeyboardButton(text="Boshqa yillar",callback_data=vote_cb.new(stage="year", id="plus", name="", number="new", language=callback_query["language"], action="branch")))
        await bot.send_message(message.from_user.id,f"{admin[1]} {admin[2]} ning  {callback_query['number']}-pazitsiya mashinasining nechinchi yillar .😉\n\nYoki yangi yil qo'shamizmi?🤨",reply_markup=markup)
    elif callback_query["language"] == "rus":
        markup.add(InlineKeyboardButton(text="Другие годы",callback_data=vote_cb.new(stage="year", id="plus", name="", number="new", language=callback_query["language"], action="branch")))
        await bot.send_message(message.from_user.id,f"{admin[1]} {admin[2]} ning  {callback_query['number']}-paditsiyalik mashinaning nechinchi yillar .😉\n\nYoki yangi yil qo'shamizmi?🤨",reply_markup=markup)
    elif callback_query["language"] == "eng":
        markup.add(InlineKeyboardButton(text="Other years",callback_data=vote_cb.new(stage="year", id="plus", name="", number="new", language=callback_query["language"], action="branch")))
        await bot.send_message(message.from_user.id,f"{admin[1]} {admin[2]} ning  {callback_query['number']}-paditsiyalik mashinaning nechinchi yillar .😉\n\nYoki yangi yil qo'shamizmi?🤨",reply_markup=markup)
    conn.execute("update ADMIN_ set paditsiya = (?) where id = (?);",(callback_query["name"],message.from_user.id))


async def admin_plus_brand(message: types.Message, conn, vote_cb, callback_query):
    conn.execute("update ADMIN_ set corporation = NULL , name = NULL, number = NULL, paditsiya = NULL ,  spare = (?) where id = (?);",(callback_query["name"],message.from_user.id))
    markup = InlineKeyboardMarkup(resize_keyboard=True)
    if callback_query["language"] == "uzb":
        markup.row(
            InlineKeyboardButton(text="⚒ Kuzov", callback_data=vote_cb.new(stage="kuzif", id="plus", name=callback_query["name"], number="", language=callback_query["language"], action="branch")),
            InlineKeyboardButton(text="⚙️ Mator", callback_data=vote_cb.new(stage="mator", id="plus", name=callback_query["name"], number="", language=callback_query["language"], action="branch")),
            InlineKeyboardButton(text="💈 Tuning", callback_data=vote_cb.new(stage="tuning", id="plus", name=callback_query["name"], number="", language=callback_query["language"], action="branch"))
        )
        await bot.send_message(message.from_user.id, f"pass", reply_markup=markup)
    elif callback_query["language"] == "rus":
        markup.row(
            InlineKeyboardButton(text="⚒ Кузов", callback_data=vote_cb.new(stage="kuzif", id="plus", name=callback_query["name"], number="", language=callback_query["language"], action="branch")),
            InlineKeyboardButton(text="⚙️ Матор", callback_data=vote_cb.new(stage="mator", id="plus", name=callback_query["name"], number="",  language=callback_query["language"],  action="branch")),
            InlineKeyboardButton(text="💈 Тюнинг", callback_data=vote_cb.new(stage="tuning", id="plus", name=callback_query["name"], number="", language=callback_query["language"], action="branch"))
        )
        car = callback_query["name"].split(',')
        await bot.send_message(message.from_user.id, f"Какую запчасть надо добавить на {callback_query['name']}-ю модель {car[0]} {car[1]}?", reply_markup=markup)
    elif callback_query["language"] == "rus":
        markup.row(
            InlineKeyboardButton(text="⚒ Body", callback_data=vote_cb.new(stage="kuzif", id="plus", name=callback_query["name"], number="", language=callback_query["language"], action="branch")),
            InlineKeyboardButton(text="⚙️ Mator", callback_data=vote_cb.new(stage="mator", id="plus", name=callback_query["name"], number="", language=callback_query["language"], action="branch")),
            InlineKeyboardButton(text="💈 Tuning", callback_data=vote_cb.new(stage="tuning", id="plus", name=callback_query["name"], number="", language=callback_query["language"], action="branch"))
        )
        car = callback_query["name"].split(',')
        await bot.send_message(message.from_user.id, f"What spare part should be added to the {callback_query['number']}rd model of the {car[0]} {car[1]}?", reply_markup=markup)


async def admin_plus_type(message: types.Message, conn, callback_query):
    conn.execute(f"update ADMIN_ set tur = (?) where id = (?);",(callback_query["stage"], message.from_user.id))
    if callback_query["language"] == "uzb":
        await bot.send_message(message.from_user.id, "Qo'shadigon maxsulotingizni shu ko'rinishida kiriting:\nNomi,Narxi")
    elif callback_query["language"] == "eng":
        await bot.send_message(message.from_user.id, "Enter the product you want to add in this view:\nName,price")
    elif callback_query["language"] == "rus":
        await bot.send_message(message.from_user.id, "Введите продукт, который вы хотите добавить, в следующем представлении:\nИмя,Цена")
