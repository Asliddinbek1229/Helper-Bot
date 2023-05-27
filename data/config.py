from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()
# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
CHANNELS = ["-1001936698333",'@biomaqsad']

KEY = [
    '/start', '/help', "🎆 Rasm fonini olib tashlash", 
     "🕋 Namoz vaqtlarini ko'rish", "🔁 Tarjimon", "✅ So'zlarni tekshirish", 
     "🗣 Speak English", "🌐 Wikipedia", "♻️ Krill-lotin"
]
