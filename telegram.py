from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Botingizning Tokenini shu yerga yozing
API_TOKEN = 'SIZNING_BOT_TOKENINGIZ_BU_YERGA'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# /start buyrug'i uchun qabul qiluvchi (handler)
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    # Foydalanuvchiga yuboriladigan xabar matni
    text = (
        "📦 Keyslar: Eng so'nggi Zamonaviy Caselar, Skinlar.\n"
        "📢 Promo: Telegram Kanalimizda E'lon Qilinadi...\n"
        "📈 Crash & Mines: Omadingizni sinab, balansingizni ko'taring!\n\n"
        "🌐 Telegram Kanalimiz : 📢 https://t.me/SSS_CreatoR_SSS"
    )
    
    # Inline tugmani yaratish
    keyboard = types.InlineKeyboardMarkup()
    
    # Vercel tarmog'idagi manzilingiz
    web_app_url = "https://creator-case-simulator.vercel.app"
    
    # Tugmaga WebApp manzilini biriktirish
    keyboard.add(types.InlineKeyboardButton(text="🚀 Start App", web_app=types.WebAppInfo(url=web_app_url)))

    # Tayyor matn va tugmani foydalanuvchiga yuborish
    await message.answer(text, reply_markup=keyboard)

# Botni ishga tushirish
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)