import telebot
from os import getenv
from dotenv import load_dotenv
from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist
from reminders.models import Month, Day, Birthday_boy, TelegramCod, Reminder
from user_reminders.models import SiteUser

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
                          'help - Информация\n'
                          'birthday - Список всех именинников\n'
                          'reminder - Ваши сообщения, напоминания\n'
                          '--------------------------------\n'
                          'Для добавления новых именинников:\n*\n'
                          'введите текст через пробел в формате\n'
                          'фамилия имя число месяц\nИванов Иван 1 10\n'
                          '---------------------------------- \n'
                          'Для добавления новых сообщений, напоминаний:\n*\n'
                          'в скобках введите сообщение, затем через пробел число и месяц \n'
                          '(сообщение) 1 10\n'
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
    TelegramCod.objects.get_or_create(telegram_cod=message.chat.id)
    for mot in month_list:
        Month.objects.get_or_create(month=mot)
    for d in range(1, 32):
        Day.objects.get_or_create(day=d)


@bot.message_handler(commands=['birthday'])
def birthday(message):
    # print(message)
    user_chat = SiteUser.objects.get(user_chat=message.chat.id)
    birthday = Birthday_boy.objects.filter(user=user_chat)
    for i in birthday:
        chat_id = message.chat.id
        bot.send_message(chat_id, i)


@bot.message_handler(commands=['reminder'])
def reminder(message):
    user_chat = SiteUser.objects.get(user_chat=message.chat.id)
    reminder = Reminder.objects.filter(user=user_chat)
    for i in reminder:
        chat_id = message.chat.id
        bot.send_message(chat_id, i)


def add_bot():
    @bot.message_handler(content_types=['text'])
    def send_text(message):
        chat_id = message.chat.id
        if '(' in message.text and ')' in message.text:
            mess_remind = message.text[message.text.find('(') + 1:message.text.find(')')]
            info_rem = (message.text).split()

            info = [mess_remind, info_rem[-2], info_rem[-1]]

            info_rem.clear()

        else:
            info = (message.text.title().split())
        try:
            day = Day.objects.get(day=info[-2])
            id = Month.objects.get(id=info[-1])
            user_chat = SiteUser.objects.get(user_chat=message.chat.id)

            if len(info) == 4:

                surname_name = Birthday_boy.objects.filter(user=user_chat, surname=info[0], name=info[1]).first()
                if not surname_name:
                    Birthday_boy.objects.create(month=id, day=day, name=info[1], surname=info[0]).user.add(user_chat.id)
                    bot.send_message(chat_id, 'Именинник успешно добавлен 😊')
                else:
                    bot.send_message(chat_id, 'У вас уже есть такой именинник\nнужно сменить фамилию или имя')

            elif len(info) == 3:
                Reminder.objects.create(month=id, day=day, reminder=info[0]).user.add(user_chat.id)
                bot.send_message(chat_id, 'Добавлено новое сообщение, напоминание 😊')

            else:
                bot.send_message(chat_id, 'Не верный формат ввода! 😔')
                bot.send_message(chat_id, 'для получения информации о правильном вводе\n'
                                          ' нужно вызвать в телеграм боте команду (иформация)/help')

        except ValueError:
            bot.send_message(chat_id, 'Нет даты или дата введена не цифрами 😔')
        except ObjectDoesNotExist:
            bot.send_message(chat_id, 'Не верный ввод ДНЯ или МЕСЯЦА рождения 😔')
        except IndexError:
            bot.send_message(chat_id, 'Не верный формат ввода 😔\n'
                                'всего одно слово или буква')

        info.clear()

    bot.polling()
