from django.db import models
from user_reminders.models import SiteUser

# class UserManager(models.Manager):
#
#     def get_queryset(self):
#         return super().get_queryset().filter(user=self.request.user)

class Day(models.Model):
    day = models.IntegerField(unique=True, db_index=True)

    def __str__(self):
        return '{}'.format(self.day)


class Month(models.Model):
    month = models.CharField(max_length=12, unique=True, db_index=True)

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
    # objects = models.Manager()
    # user_objects = UserManager()
    name = models.CharField(max_length=32, default='no name')
    surname = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.surname} {self.name}   ({self.day} : {self.month})'

    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    user = models.ManyToManyField(SiteUser)

