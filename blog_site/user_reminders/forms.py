from django.contrib.auth.forms import UserCreationForm

from reminders.models import TelegramCod
from .models import SiteUser
from django.utils.translation import gettext_lazy as _


class RegistrationForm(UserCreationForm):

    def clean(self):
        super(RegistrationForm, self).clean()
        user_chat = self.cleaned_data.get('user_chat')
        cod_in_db = TelegramCod.objects.filter(telegram_cod=user_chat).first()
        if not cod_in_db:
            self._errors['user_chat'] = self.error_class([
                'Код не найден! ( Введите код из бота )'])

        return self.cleaned_data

    class Meta:
        model = SiteUser
        fields = ['username', 'password1', 'password2', 'email', 'image', 'user_chat']
        labels = {
            'user_chat': _('Код из телеграм(10-цифр)'),
            'image': _('Фото профиля (необезательно)'),

        }
