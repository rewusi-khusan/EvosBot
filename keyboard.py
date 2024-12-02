from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🍴 Menyu',),
        ],
        [
            KeyboardButton(text='🛍 Mening buyurtmalarim'),
        ],
        [
            KeyboardButton(text='✍️ Fikr bildirish'),
            KeyboardButton(text='⚙️ Sozlamalar'),
        ],
    ],
    resize_keyboard=True,
)

evos_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🗺 Mening manzillarim')
        ],
        [
            KeyboardButton(text='🏠 Bosh sahifa')
        ]
    ],
    resize_keyboard=True,
)

comment = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🏠 Bosh sahifa')
        ]
    ],
    resize_keyboard=True,
)

setting = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Tilni o'zgartirish")
        ],
        [
            KeyboardButton(text='🏠 Bosh sahifa')
        ]
    ],
    resize_keyboard=True,
)

address = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Yunusobod MARS IT School')
        ],
        [
            KeyboardButton(text='Yunusobod 4-kvartal, 12')
        ],
        [
            KeyboardButton(text='🏠 Bosh sahifa')
        ]
    ],
    resize_keyboard=True,
)

opros = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="❌ Yo'q"),
            KeyboardButton(text='✅ Ha')
        ],
        [
            KeyboardButton(text='🏠 Bosh sahifa')
        ]
    ],
    resize_keyboard=True,
)

bolim = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Aksiya'),
            KeyboardButton('Setlar va juftliklar')
        ],
        [
            KeyboardButton('Lavash'),
            KeyboardButton('Trindwich')
        ],
        [
            KeyboardButton('Shaurma'),
            KeyboardButton('Burger')
        ],
        [
            KeyboardButton('Sub'),
            KeyboardButton('Kartoshka')
        ],
        [
            KeyboardButton('Hot Dog'),
            KeyboardButton('Sneiklar')
        ],
        [
            KeyboardButton('Salat, garnir, non'),
            KeyboardButton('Souslar')
        ],
        [
            KeyboardButton('Taom'),
            KeyboardButton('Desertlar')
        ],
        [
            KeyboardButton('Issiq ichimliklar'),
            KeyboardButton('Sovuq ichimliklar')
        ],
        [
            KeyboardButton('Combo')
        ],
        [
            KeyboardButton('🏠 Bosh sahifa')
        ]
    ],
    resize_keyboard=True
)

aks = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('2 Лаваша с говядиной и сыром'),
            KeyboardButton('2 Триндвича с говядиной')
        ],
        [
            KeyboardButton('2 Салата Греческих'),
            KeyboardButton('2 Салата Цезарь')
        ],
        [
            KeyboardButton('2 Картошки фри'),
        ],
        [
            KeyboardButton("📘 Bo'limlarga qaytish"),
            KeyboardButton('🏠 Bosh sahifa')
        ]
    ],
    resize_keyboard=True,
)

set = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Fit-Plus 2'),
            KeyboardButton('Fit-Plus 3'),
        ],
        [
            KeyboardButton('Fri Plus'),
            KeyboardButton('Fri Plus 7up'),
        ],
        [
            KeyboardButton('Fit-Plus 1'),
            KeyboardButton('Double Set 2'),
        ],
        [
            KeyboardButton('Double Set 1'),
            KeyboardButton('Oilaviy Set 1'),
        ],
        [
            KeyboardButton("📘 Bo'limlarga qaytish"),
            KeyboardButton('🏠 Bosh sahifa')
        ]
    ],
    resize_keyboard=True,
)

lavash = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Fitter'),
            KeyboardButton("Mol go'shtidan qalampir lavash"),
        ],
        [
            KeyboardButton("Tovuq go'shtidan qalampir lavash"),
            KeyboardButton("Mol go'shtidan qalampir lavash"),
        ],
        [
            KeyboardButton("Tovuq go`shtidan lavash"),
        ],
        [
            KeyboardButton("📘 Bo'limlarga qaytish"),
            KeyboardButton('🏠 Bosh sahifa')
        ]
    ],
    resize_keyboard=True,
)

trind = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('2 Триндвича с говядиной'),
            KeyboardButton("Trindwich mol go'shtidan"),
        ],
        [
            KeyboardButton("Trindwich tovuq go'shtidan"),
        ],
        [
            KeyboardButton("📘 Bo'limlarga qaytish"),
            KeyboardButton('🏠 Bosh sahifa')
        ]
    ],
    resize_keyboard=True,
)

shaur = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Mol go'shtidan shaurma"),
            KeyboardButton("Tovuq go'shtidan shaurma"),
        ],
        [
            KeyboardButton("Tovuq go'shtidan qalampir shaurma"),
            KeyboardButton("Mol go'shtidan qalampir shaurma")
        ],
        [
            KeyboardButton("📘 Bo'limlarga qaytish"),
            KeyboardButton('🏠 Bosh sahifa')
        ]
    ],
    resize_keyboard=True,
)

bur = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Gamburger"),
            KeyboardButton("Chizburger")
        ],
        [
            KeyboardButton("Dablburger"),
            KeyboardButton("Dablchizburger")
        ],
        [
            KeyboardButton('Kids-Kvadrich'),
        ],
        [
            KeyboardButton("📘 Bo'limlarga qaytish"),
            KeyboardButton('🏠 Bosh sahifa')
        ]
    ],
    resize_keyboard=True,
)

sub = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Mol go`shtidan sab"),
            KeyboardButton("Tovuq go`shtidan sab"),
        ],
        [
            KeyboardButton("Mol go`shtidan pishloqli sab"),
            KeyboardButton("Tovuq go`shtidan pishloqli sab"),
        ],
        [
            KeyboardButton("📘 Bo'limlarga qaytish"),
            KeyboardButton('🏠 Bosh sahifa')
        ]
    ],
    resize_keyboard=True,
)

kar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Naggetslar, 4 dona"),
            KeyboardButton("Naggetslar, 8 dona"),
        ],
        [
            KeyboardButton("Kartoshka Fri Mini"),
            KeyboardButton('Kartoshka Fri'),
        ],
        [
            KeyboardButton("Jaydari kartoshka"),
        ],
        [
            KeyboardButton("📘 Bo'limlarga qaytish"),
            KeyboardButton('🏠 Bosh sahifa')
        ]
    ],
    resize_keyboard=True,
)

hot = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Hot-Dog"),
            KeyboardButton("Hot-Dog-Dabl"),
        ],
        [
            KeyboardButton("Hot-Dog Mini"),
            KeyboardButton("Bolalar uchun Hot-Dog"),
        ],
        [
            KeyboardButton("📘 Bo'limlarga qaytish"),
            KeyboardButton('🏠 Bosh sahifa')
        ]
    ],
    resize_keyboard=True,
)

snek = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Strips'),
            KeyboardButton('Smayliki'),
        ],
        [
            KeyboardButton("📘 Bo'limlarga qaytish"),
            KeyboardButton('🏠 Bosh sahifa')
        ]
    ],
    resize_keyboard=True,
)

salat = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Sezar salat'),
            KeyboardButton('Grecheskiy salat'),
        ],
        [
            KeyboardButton('2 Салата Греческих'),
            KeyboardButton('2 Салата Цезарь')
        ],
        [
            KeyboardButton('Non'),
            KeyboardButton('Guruch'),
        ],
        [
            KeyboardButton("📘 Bo'limlarga qaytish"),
            KeyboardButton('🏠 Bosh sahifa')
        ]
    ],
    resize_keyboard=True,
)

sous = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Sezar sous'),
            KeyboardButton('Grecheskiy sous'),
        ],
        [
            KeyboardButton('Pishloqli sous'),
            KeyboardButton('Sarimsoqli sous'),
        ],
        [
            KeyboardButton('Chili sous'),
            KeyboardButton('Barbekyu sousi'),
        ],
        [
            KeyboardButton('Ketchup'),
            KeyboardButton('Mayonez'),
        ],
        [
            KeyboardButton("📘 Bo'limlarga qaytish"),
            KeyboardButton('🏠 Bosh sahifa')
        ]
    ],
    resize_keyboard=True,
)

taom = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Mol go'shtidan donar"),
            KeyboardButton("Tovuq go'shtidan donar"),
        ],
        [
            KeyboardButton("Donar-box mol go'shtli"),
            KeyboardButton("Donar-box tovuq go'shtli"),
        ],
        [
            KeyboardButton("📘 Bo'limlarga qaytish"),
            KeyboardButton('🏠 Bosh sahifa')
        ]
    ],
    resize_keyboard=True,
)

desert = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Karameli donut'),
            KeyboardButton('Medovik (Asalli tort)'),
        ],
        [
            KeyboardButton('Chizkeyk'),
            KeyboardButton("Mevali Donut"),
        ],
        [
            KeyboardButton("📘 Bo'limlarga qaytish"),
            KeyboardButton('🏠 Bosh sahifa')
        ]
    ],
    resize_keyboard=True,
)

issiq = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Kapuchino"),
            KeyboardButton("Kofe Glyase")
        ],
        [
            KeyboardButton("Limonli qora choy"),
            KeyboardButton("Kofe Latte")
        ],
        [
            KeyboardButton("Amerikano"),
            KeyboardButton("Ko’k choy")
        ],
        [
            KeyboardButton("Qora choy"),
            KeyboardButton("Limonli ko’k choy")
        ],
        [
            KeyboardButton("📘 Bo'limlarga qaytish"),
            KeyboardButton('🏠 Bosh sahifa')
        ]
    ],
    resize_keyboard=True,
)


sovuq = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Pepsi 0,5L"),
            KeyboardButton("Pepsi 1,5L"),
        ],
        [
            KeyboardButton("Mirinda razliv"),
            KeyboardButton("Pepsi razliv"),
        ],
        [
            KeyboardButton("Olmali sharbat shakarsiz, 0,33L"),
            KeyboardButton("Apelsinli sharbat, 1 L"),
        ],
        [
            KeyboardButton("Olchali sharbat, 1 L"),
            KeyboardButton("Gazlangan suv 0.5L"),
        ],
        [
            KeyboardButton("7up razliv"),
            KeyboardButton("Pina colada"),
        ],
        [
            KeyboardButton("Moxito")
        ],
        [
            KeyboardButton("📘 Bo'limlarga qaytish"),
            KeyboardButton('🏠 Bosh sahifa')
        ]
    ],
    resize_keyboard=True,
)

combo = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Talaba-Combo'),
            KeyboardButton('S-Combo №1'),
        ],
        [
            KeyboardButton('S-Combo №2'),
            KeyboardButton('S-Combo №3'),
        ],
        [
            KeyboardButton('S-Combo №4'),
            KeyboardButton('M-Combo 1'),
        ],
        [
            KeyboardButton('M-Combo 2'),
            KeyboardButton('M-Combo 3'),
        ],
        [
            KeyboardButton('M-Combo 4'),
            KeyboardButton('M-Combo 5'),
        ],
        [
            KeyboardButton("Bolalar uchun Combo")
        ],
        [
            KeyboardButton("📘 Bo'limlarga qaytish"),
            KeyboardButton('🏠 Bosh sahifa')
        ]
    ],
    resize_keyboard=True,
)

count = 1
product = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='-', callback_data='minus'),
            InlineKeyboardButton(text=str(count), callback_data='count'),
            InlineKeyboardButton(text='+', callback_data='plus')
        ],
        [
            InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data='add')
        ]
    ]
)



