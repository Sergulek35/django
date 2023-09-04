from django import forms
from django.utils.translation import gettext_lazy as _
from reminders.models import Birthday_boy, User, Reminder


class HumanCodForm(forms.Form):
    user_cod = forms.IntegerField(label='Ваш код')

    def clean(self):
        super(HumanCodForm, self).clean()
        user_cod = self.cleaned_data.get('user_cod')
        cod_in_db = User.objects.filter(user_chat=user_cod).first()
        if not cod_in_db:
            self._errors['user_cod'] = self.error_class([
                'Код не найден! ( Введите код из бота )'])

        return self.cleaned_data


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
