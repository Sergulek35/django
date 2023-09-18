from django.db import models

from user_reminders.models import SiteUser


class Day(models.Model):
    day = models.IntegerField(unique=True)

    def __str__(self):
        return '{}'.format(self.day)


class Month(models.Model):
    month = models.CharField(max_length=12, unique=True)

    def __str__(self):
        return self.month


class TelegramCod(models.Model):
    telegram_cod = models.PositiveIntegerField(unique=True)


class Reminder(models.Model):
    reminder = models.TextField()

    def __str__(self):
        return f'[  {self.reminder}  ] - напомнить - ({self.day} : {self.month})'

    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    user = models.ManyToManyField(SiteUser)


class Birthday_boy(models.Model):
    name = models.CharField(max_length=32, default='default name')
    surname = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.surname} {self.name}   ({self.day} : {self.month})'

    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    user = models.ManyToManyField(SiteUser)
