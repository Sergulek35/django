import telebot
from os import getenv
from dotenv import load_dotenv
from django.core.management.base import BaseCommand
from reminders.models import Birthday_boy, User
from datetime import datetime
import requests

load_dotenv()

TOKEN = getenv('token')
bot = telebot.TeleBot(TOKEN)

date_time = datetime.now()
date_now = float(f'{date_time.day}.{date_time.month}')  # текущая дата


class Command(BaseCommand):

    def handle(self, *args, **options):
        date_time()


def date_time():
    # Если даты совпадают, отправляем сообщение
    user_chat = User.objects.all()
    for us in user_chat:
        # print(us.user_chat)
        for i in Birthday_boy.objects.filter(user=us.id):
            date_birthday = float(f'{int(i.day)}.{i.month.id}')
            print(date_birthday)
            if date_birthday == date_now:
                chat_id = us.user_chat
                message = f'{i.surname} {i.name} - празднует сегодня день рождения\n' \
                          f'-------------\nПоздравьте 🎁'

                url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
                requests.get(url).json()  # отправляем
