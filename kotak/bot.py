import telebot
import os
from django.core.wsgi import get_wsgi_application
import django

# Инициализация Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kotak.settings")
django.setup()

from cats.models import Cat  # Импортируем модель котов

# Токен твоего бота
bot = telebot.TeleBot("7246315755:AAFCfXB4RFz3HhsRR8b3p8H1Q_fU5e7OBM0")

# Считывание всех котиков из базы данных
cats = Cat.objects.all()  # Список всех котов в базе данных
cat_index = 0  # Индекс текущего кота

@bot.message_handler(commands=['start'])
def send_welcome(message):
    """Отправить приветственное сообщение и кнопку"""
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    item = telebot.types.KeyboardButton("Какой я сегодня кот?")
    markup.add(item)
    bot.send_message(message.chat.id, "Йоууу! Я бот котак. Нажми кнопку, чтобы узнать, какой ты кот сегодня!", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Какой я сегодня кот?")
def send_cat(message):
    global cat_index  # Используем глобальную переменную для отслеживания текущего кота

    if cat_index >= len(cats):  # Если дошли до последнего кота, начинаем заново
        cat_index = 0

    # Получаем текущего кота
    cat = cats[cat_index]
    image_path = cat.image.path
    message_text = cat.message

    # Отправляем картинку с текстом
    with open(image_path, 'rb') as img:
        bot.send_photo(message.chat.id, img, caption=message_text)

    # Увеличиваем индекс для следующего кота
    cat_index += 1

bot.polling()
