from datetime import datetime

from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from .forms import HumanForm, HumanCodForm, MessagesForm
from reminders.models import Birthday_boy, User, Reminder
from django.views.generic import ListView, CreateView,DeleteView
from django.views.generic.base import ContextMixin
from django.views.generic.edit import FormView

in_flag = bool
user_cod_id = []
date_time = datetime.now()


class RadmiHumanView(FormView):
    form_class = HumanCodForm

    success_url = reverse_lazy('blog_site:index')
    template_name = 'reminders/radmi_human.html'

    def form_valid(self, form):
        user_cod_id.clear()
        user_cod = form.cleaned_data['user_cod']
        user_chat = User.objects.get(user_chat=user_cod)
        user_cod_id.append(user_chat.id)
        user_cod_id.append(user_chat)

        return super().form_valid(form)


class HumanContextMixin(ContextMixin):

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['in_flag'] = True
        context['count'] = Birthday_boy.objects.filter(user=user_cod_id[0]).count()
        context['count_messages'] = Reminder.objects.filter(user=user_cod_id[0]).count()
        context['user_chat'] = user_cod_id[1]
        context['date_time'] = date_time.date()

        return context


class RadmiIndexView(ListView, HumanContextMixin):
    model = Birthday_boy
    template_name = 'reminders/index.html'
    context_object_name = 'user_chat'
    context_object_name = 'date_time'


class RadmiListView(ListView, HumanContextMixin):
    model = Birthday_boy
    template_name = 'reminders/radmi_list.html'
    context_object_name = 'birthday'

    def get_queryset(self):
        return Birthday_boy.objects.filter(user=user_cod_id[0])



class RadmiCreateView(CreateView, HumanContextMixin):
    form_class = HumanForm

    success_url = reverse_lazy('blog_site:index')
    template_name = 'reminders/radmi_create.html'

    def form_valid(self, form):
        month = form.cleaned_data['month']
        day = form.cleaned_data['day']
        name = form.cleaned_data['name'].title()
        surname = form.cleaned_data['surname'].title()

        Birthday_boy.objects.create(month=month, day=day, name=name, surname=surname).user.add(user_cod_id[0])

        return super().form_valid(form)


class RadmiDeleteView(DeleteView, HumanContextMixin):
    model = Birthday_boy
    template_name = 'reminders/radmi_delete.html'
    success_url = reverse_lazy('blog_site:radmi_list')


class MessagListView(ListView, HumanContextMixin):
    model = Reminder
    template_name = 'reminders/messages.html'
    context_object_name = 'reminder'

    def get_queryset(self):
        return Reminder.objects.filter(user=user_cod_id[0])


class MessagCreateView(CreateView, HumanContextMixin):
    form_class = MessagesForm

    success_url = reverse_lazy('blog_site:index')
    template_name = 'reminders/messages_create.html'

    def form_valid(self, form):
        month = form.cleaned_data['month']
        day = form.cleaned_data['day']
        reminder = form.cleaned_data['reminder']

        Reminder.objects.create(month=month, day=day, reminder=reminder).user.add(user_cod_id[0])

        return super().form_valid(form)


class MessagDeleteView(DeleteView, HumanContextMixin):
    model = Reminder
    template_name = 'reminders/messages_delete.html'
    success_url = reverse_lazy('blog_site:messages')
