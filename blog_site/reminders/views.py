from datetime import datetime
from django.urls import reverse_lazy
from .forms import HumanForm, MessagesForm
from reminders.models import Birthday_boy, Reminder
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.views.generic.base import ContextMixin


date_time = datetime.now()

class HumanContextMixin(ContextMixin):

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = Birthday_boy.objects.filter(user=self.request.user).count()
        context['count_messages'] = Reminder.objects.filter(user=self.request.user).count()
        context['date_time'] = date_time.date()

        return context


class RadmiIndexView(ListView, HumanContextMixin):
    model = Birthday_boy
    template_name = 'reminders/index.html'
    context_object_name = 'date_time'


class RadmiListView(ListView, HumanContextMixin):
    model = Birthday_boy
    template_name = 'reminders/radmi_list.html'
    context_object_name = 'birthday'

    def get_queryset(self):
        return Birthday_boy.objects.filter(user=self.request.user)


class RadmiCreateView(CreateView, HumanContextMixin):
    form_class = HumanForm

    success_url = reverse_lazy('blog_site:index')
    template_name = 'reminders/radmi_create.html'

    def form_valid(self, form):
        month = form.cleaned_data['month']
        day = form.cleaned_data['day']
        name = form.cleaned_data['name'].title()
        surname = form.cleaned_data['surname'].title()

        Birthday_boy.objects.create(month=month, day=day, name=name, surname=surname).user.add(self.request.user)

        return super().form_valid(form)


class RadmiDeleteView(DeleteView, HumanContextMixin):
    model = Birthday_boy
    template_name = 'reminders/radmi_delete.html'
    success_url = reverse_lazy('blog_site:radmi_list')


class MessagListView(ListView, HumanContextMixin):
    model = Reminder
    template_name = 'reminders/messages.html'
    context_object_name = 'reminder'
    paginate_by = 1

    def get_queryset(self):
        return Reminder.objects.filter(user=self.request.user)


class MessagCreateView(CreateView, HumanContextMixin):
    form_class = MessagesForm

    success_url = reverse_lazy('blog_site:index')
    template_name = 'reminders/messages_create.html'

    def form_valid(self, form):
        month = form.cleaned_data['month']
        day = form.cleaned_data['day']
        reminder = form.cleaned_data['reminder']

        Reminder.objects.create(month=month, day=day, reminder=reminder).user.add(self.request.user)

        return super().form_valid(form)


class MessagDeleteView(DeleteView, HumanContextMixin):
    model = Reminder
    template_name = 'reminders/messages_delete.html'
    success_url = reverse_lazy('blog_site:messages')


class MessagUpdataView(UpdateView, HumanContextMixin):
    fields = ['reminder', 'day', 'month']

    model = Reminder
    success_url = reverse_lazy('blog_site:messages')
    template_name = 'reminders/messages_create.html'


class RadmiUpdataView(UpdateView, HumanContextMixin):

    fields = ['surname', 'name', 'day', 'month']
    model = Birthday_boy

    success_url = reverse_lazy('blog_site:radmi_list')
    template_name = 'reminders/radmi_create.html'



