from aiogram import Bot, Dispatcher, types, executor
from keyboard import menu, evos_menu, comment, address, opros, bolim, aks, set, lavash, trind, shaur, bur, sub, kar,  hot, snek, salat, sous, taom, desert, issiq, sovuq, combo, setting
from mahsulotlar import mahsulot
from keyboard import product

token = '7134139366:AAFq9oO0l2zdve-fjMDvDYCXMjgiwn3YIaU'
bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(text="Quyidagilardan birini tanlang!", reply_markup=menu)

@dp.message_handler(text='🍴 Menyu')
async def evos(message: types.Message):
    await message.answer(text="📍 Geolokatsiyani yuboring yoki yetkazib berish manzilini tanlang", reply_markup=evos_menu)

@dp.message_handler(text='✍️ Fikr bildirish')
async def evos(message: types.Message):
    await message.answer(text="Fikringizni yuboring", reply_markup=comment)

@dp.message_handler(text='🛍 Mening buyurtmalarim')
async def evos(message: types.Message):
    await message.answer(text="Siz hech narsa buyurtma bermagansiz!", reply_markup=menu)

@dp.message_handler(text='⚙️ Sozlamalar')
async def settings(message: types.Message):
    await message.answer(text="Buyruqni tanlang:", reply_markup=setting)

@dp.message_handler(text="Tilni o'zgartirish")
async def lang(message: types.Message):
    await message.answer(text="Uzr, hozircha bu funksiya mavjud emas!")

@dp.message_handler(text='🗺 Mening manzillarim')
async def evos(message: types.Message):
    await message.answer(text="Yetkazib berish manzilni tanlang", reply_markup=address)

@dp.message_handler(text='Yunusobod MARS IT School')
async def location(message: types.Message):
    latt = 41.36726636799181
    long = 69.28606999261169
    await message.answer_location(latitude=latt, longitude=long)
    await message.answer(text='Siz manzilni tasdiqlaysizmi?', reply_markup=opros)

@dp.message_handler(text='Yunusobod 4-kvartal, 12')
async def location2(message: types.Message):
    latt = 41.365368
    long = 69.283779
    await message.answer_location(latitude=latt, longitude=long)
    await message.answer(text='Siz manzilni tasdiqlaysizmi?', reply_markup=opros)

@dp.message_handler(content_types=types.ContentType.LOCATION)
async def loc(message: types.Message):
    await message.answer(text='Siz manzilni tasdiqlaysizmi?', reply_markup=opros)

@dp.message_handler(text="❌ Yo'q")
async def no(message: types.Message):
    await message.answer(text="Boshqa manzilni tanlang!", reply_markup=address)

@dp.message_handler(text='✅ Ha')
async def yes(message: types.Message):
    await message.answer(text="Bo'limni tanlang!", reply_markup=bolim)


@dp.message_handler(text='Aksiya')
async def aksiya(message: types.Message):
    photo = types.InputFile('media/aksiya_glavniy.jpg')
    await message.answer_photo(photo, reply_markup=aks)

@dp.message_handler(text='Setlar va juftliklar')
async def setlar(message: types.Message):
    photo = types.InputFile('media/set_glavniy.jpg')
    await message.answer_photo(photo, reply_markup=set)

@dp.message_handler(text='Lavash')
async def lav(message: types.Message):
    photo = types.InputFile('media/lavash_glavniy.jpg')
    await message.answer_photo(photo, reply_markup=lavash)

@dp.message_handler(text='Trindwich')
async def trindwich(message: types.Message):
    photo = types.InputFile('media/trind_glavniy.jpg')
    await message.answer_photo(photo, reply_markup=trind)

@dp.message_handler(text='Shaurma')
async def shaurma(message: types.Message):
    photo = types.InputFile('media/shaurma_glavniy.jpg')
    await message.answer_photo(photo, reply_markup=shaur)

@dp.message_handler(text='Burger')
async def burger(message: types.Message):
    photo = types.InputFile('media/burger_glavniy.jpg')
    await message.answer_photo(photo, reply_markup=bur)

@dp.message_handler(text='Sub')
async def sab(message: types.Message):
    photo = types.InputFile('media/sub_glavniy.jpg')
    await message.answer_photo(photo, reply_markup=sub)

@dp.message_handler(text='Kartoshka')
async def kartoshka(message: types.Message):
    photo = types.InputFile('media/kartoshka_glavniy.jpg')
    await message.answer_photo(photo, reply_markup=kar)

@dp.message_handler(text='Hot Dog')
async def hotdog(message: types.Message):
    photo = types.InputFile('media/hotdog_glavniy.jpg')
    await message.answer_photo(photo, reply_markup=hot)

@dp.message_handler(text='Sneiklar')
async def sneik(message: types.Message):
    photo = types.InputFile('media/snek_glavniy.jpg')
    await message.answer_photo(photo, reply_markup=snek)

@dp.message_handler(text='Souslar')
async def souslar(message: types.Message):
    photo = types.InputFile('media/sous_glavniy.jpg')
    await message.answer_photo(photo, reply_markup=sous)

@dp.message_handler(text='Taom')
async def taomlar(message: types.Message):
    photo = types.InputFile('media/taom_glavniy.jpg')
    await message.answer_photo(photo, reply_markup=taom)

@dp.message_handler(text='Desertlar')
async def desertlar(message: types.Message):
    photo = types.InputFile('media/desert_glavniy.jpg')
    await message.answer_photo(photo, reply_markup=desert)

@dp.message_handler(text='Salat, garnir, non')
async def non(message: types.Message):
    photo = types.InputFile('media/salat_glavniy.jpg')
    await message.answer_photo(photo, reply_markup=salat)

@dp.message_handler(text='Issiq ichimliklar')
async def issiqlar(message: types.Message):
    photo = types.InputFile('media/issiq_glavniy.jpg')
    await message.answer_photo(photo, reply_markup=issiq)

@dp.message_handler(text='Sovuq ichimliklar')
async def sovuqlar(message: types.Message):
    photo = types.InputFile('media/sovuq_glavniy.jpg')
    await message.answer_photo(photo, reply_markup=sovuq)

@dp.message_handler(text='Combo')
async def combolar(message: types.Message):
    photo = types.InputFile('media/combo_glavniy.jpg')
    await message.answer_photo(photo, reply_markup=combo)

@dp.message_handler(text='🏠 Bosh sahifa')
async def back(message: types.Message):
    await message.answer(text="Menyuga qaytish", reply_markup=menu)

@dp.message_handler(text="📘 Bo'limlarga qaytish")
async def bolimga_qaytish(message: types.Message):
    await message.answer(text="Bo'limlarga qaytish", reply_markup=bolim)

@dp.message_handler()
async def mah(message: types.Message):
    for i in mahsulot.keys():
        if i.lower() == message.text.lower():
            photo = types.InputFile(f'media/{message.text}.jpg')
            await message.answer_photo(photo=photo, caption=mahsulot[i], reply_markup=product)
    else:
        pass

@dp.callback_query_handler(text='minus')
async def handle_callback(callback_query: types.CallbackQuery):
    count = int(product.inline_keyboard[0][1].text)

    if count > 1:
        count -= 1

    product.inline_keyboard[0][1].text = str(count)

    await callback_query.message.edit_reply_markup(reply_markup=product)



@dp.callback_query_handler(text='plus')
async def handle_callback(callback_query: types.CallbackQuery):
    count = int(product.inline_keyboard[0][1].text)

    count += 1

    product.inline_keyboard[0][1].text = str(count)

    await callback_query.message.edit_reply_markup(reply_markup=product)


@dp.callback_query_handler(text='add')
async def handle_callback(callback_query: types.CallbackQuery):
    await callback_query.message.answer("Mahsulot savatga qo'shildi")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
