from django import forms
from django.utils.translation import gettext_lazy as _
from reminders.models import Birthday_boy, Reminder

class HumanForm(forms.ModelForm):
    name = forms.CharField(label='Имя', max_length=32)

    class Meta:
        model = Birthday_boy
        fields = ['surname', 'name', 'day', 'month']

        labels = {
            'surname': _('Фамилия'),
            'name': _('Имя'),
            'day': _('Число'),
            'month': _('Месяц'),
        }

class MessagesForm(forms.ModelForm):

    class Meta:
        model = Reminder
        fields = ['reminder', 'day', 'month']

        labels = {

            'day': _('Число'),
            'month': _('Месяц'),
            'reminder': _('Сообщение')
        }
