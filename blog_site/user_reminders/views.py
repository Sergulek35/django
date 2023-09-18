import requests
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from reminders.management.commands.remind import TOKEN
from .forms import RegistrationForm
from django.views.generic import CreateView
from .models import SiteUser

class UserLoginView(LoginView):
    template_name = 'user_reminders/login.html'


class UserCreateView(CreateView):
    model = SiteUser
    template_name = 'user_reminders/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user_chat = form.cleaned_data['user_chat']
        message = 'Регистрация на сайте прошла успешно!'
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={user_chat}&text={message}"
        requests.get(url).json()  # отправляем

        return super().form_valid(form)
