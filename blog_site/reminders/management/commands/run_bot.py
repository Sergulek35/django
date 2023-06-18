import telebot
from os import getenv
from dotenv import load_dotenv
from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist
from reminders.models import Month, Day, Birthday_boy, User

load_dotenv()

TOKEN = getenv('token')
bot = telebot.TeleBot(TOKEN)

month_list = ['Января', 'Февраля', 'Марта', 'Апреля', 'Мая', 'Июня', 'Июля', 'Августа', 'Сентября',
              'Октября', 'Ноября', 'Декабря']


class Command(BaseCommand):


    def handle(self, *args, **options):
        add_bot()


@bot.message_handler(commands=['help'])
def examination(message):
    # print(message)
    bot.reply_to(message, 'команды:\nstart - Регистрация\n'
                          'help - Помощь\n'
                          'birthday - Список всех именинников\n'
                          '--------------------------------\n'
                          'Для добавления новых именинников \n'
                          'введите текст через пробел в формате\n'
                          '(фамилия имя число месяц)\n(Иванов Иван 1 10)\n'
                          '🤝')


@bot.message_handler(commands=['start'])
def examination(message):
    # print(message)
    hey = message.from_user.first_name
    bot.reply_to(message, f'Добро пожаловать, {hey}\n'
                          f'-------------------------------- \n'
                          f'Ваш код для сайта {message.chat.id}\n'
                          f'👋')
    # print(message.chat.id)
    User.objects.get_or_create(user_name=hey, user_chat=message.chat.id)
    for mot in month_list:
        Month.objects.get_or_create(month=mot)
    for d in range(1, 32):
        Day.objects.get_or_create(day=d)


@bot.message_handler(commands=['birthday'])
def birthday(message):
    # print(message)
    user_chat = User.objects.get(user_chat=message.chat.id)
    birthday = Birthday_boy.objects.filter(user=user_chat)
    for i in birthday:
        chat_id = message.chat.id
        bot.send_message(chat_id, i)


def add_bot():
    @bot.message_handler(content_types=['text'])
    def send_text(message):
        info = (message.text.title().split())
        chat_id = message.chat.id
        try:
            if len(info) != 4:
                bot.send_message(chat_id, 'Не верный формат ввода')
                bot.send_message(chat_id, 'введите текст через пробел в формате\n'
                                          '(фамилия имя число месяц)\n(Иванов Иван 1 10)\n')
            elif info[2] == '0' or int(info[2]) > 31:
                bot.send_message(chat_id, 'Не верный ввод ДНЯ рождения')

            else:

                day = Day.objects.get(day=info[2])
                id = Month.objects.get(id=info[3])
                user_chat = User.objects.get(user_chat=message.chat.id)

                surname_name = Birthday_boy.objects.filter(user=user_chat, surname=info[0], name=info[1]).first()
                if not surname_name:
                    Birthday_boy.objects.create(month=id, day=day, name=info[1], surname=info[0]).user.add(user_chat.id)
                    bot.send_message(chat_id, 'Именинник успешно добавлен!')
                else:
                    bot.send_message(chat_id, 'У вас уже есть такой именинник\nнужно сменить фамилию или имя')
        except ValueError:
            bot.send_message(chat_id, 'Число и месяц нужно вводить цифрами')
        except ObjectDoesNotExist:
            bot.send_message(chat_id, 'Не верный ввод МЕСЯЦА рождения')

        info.clear()

    bot.polling()
