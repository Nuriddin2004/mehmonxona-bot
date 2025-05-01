import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = '8124838645:AAFsWkBBqkusLVLy2fhfaXi4-kNjo1d-GSM'  # Bot token
bot = telebot.TeleBot(TOKEN)

# /start komandasi
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    phone_btn = KeyboardButton("📞 Nomer orqali ro'yxatdan o'tish", request_contact=True)
    markup.add(phone_btn)
    bot.send_message(message.chat.id, "Xush kelibsiz! Ro'yxatdan o'tish uchun nomeringizni yuboring:", reply_markup=markup)

# Kontakt yuborilganda
@bot.message_handler(content_types=['contact'])
def handle_contact(message):
    user_phone = message.contact.phone_number
    bot.send_message(message.chat.id, f"Rahmat! Siz muvaffaqiyatli ro'yxatdan o'tdingiz.\nTelefon raqamingiz: {user_phone}")

    # Endi foydalanuvchidan ariza yoki taklif tanlashni so‘raymiz
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("📝 Ariza qoldirish", "💡 Taklif bildirish")
    bot.send_message(message.chat.id, "Iltimos, quyidagilardan birini tanlang:", reply_markup=markup)

# Ariza yoki taklif tanlanganda
@bot.message_handler(func=lambda message: message.text in ["📝 Ariza qoldirish", "💡 Taklif bildirish"])
def ask_for_text(message):
    if message.text == "📝 Ariza qoldirish":
        bot.send_message(message.chat.id, "Arizangizni yozing:")
        bot.register_next_step_handler(message, save_ariza)
    else:
        bot.send_message(message.chat.id, "Taklifingizni yozing:")
        bot.register_next_step_handler(message, save_taklif)

def save_ariza(message):
    # Arizani bazaga saqlash yoki adminga yuborish mumkin
    bot.send_message(message.chat.id, "Arizangiz qabul qilindi. Rahmat!")

def save_taklif(message):
    bot.send_message(message.chat.id, "Taklifingiz uchun rahmat!")

bot.infinity_polling()
