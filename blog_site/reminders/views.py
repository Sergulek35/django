from django.shortcuts import render
from datetime import datetime
from .forms import HumanForm, HumanCodForm
from reminders.models import Birthday_boy, User


in_flag = bool
user_cod_id = []
date_time = datetime.now()


def index(request):

    if request.method == 'POST':
        form_in = HumanCodForm(request.POST)
        if form_in.is_valid():

            in_flag = True

            user_cod = form_in.cleaned_data['user_cod']
            user_chat = User.objects.get(user_chat=user_cod)
            user_cod_id.append(user_chat.id)

            return render(request, 'reminders/index.html', context={'in_flag': in_flag, 'date_time': date_time,
                                                                    'user_chat': user_chat})

        else:

            return render(request, 'reminders/index.html', context={'form_in': form_in})

    else:
        user_cod_id.clear()
        form_in = HumanCodForm()
        return render(request, 'reminders/index.html', context={'form_in': form_in})


def create_person(request):
    in_flag = True
    if request.method == 'POST':

        form = HumanForm(request.POST)

        if form.is_valid():

            month = form.cleaned_data['month']
            day = form.cleaned_data['day']
            name = form.cleaned_data['name'].title()
            surname = form.cleaned_data['surname'].title()

            Birthday_boy.objects.create(month=month, day=day, name=name, surname=surname).user.add(user_cod_id[0])
            story = f'{surname}  {name}  - ДОБАВЛЕН'

            return render(request, 'reminders/index.html', context={'in_flag': in_flag, 'date_time': date_time,
                                                                    'story': story})

        else:
            return render(request, 'reminders/create.html', context={'in_flag': in_flag, 'form': form})

    else:
        form = HumanForm()
        return render(request, 'reminders/create.html', context={'in_flag': in_flag, 'form': form})


def delete_person(request):
    in_flag = True
    birthday = Birthday_boy.objects.filter(user=user_cod_id[0])

    if request.method == 'POST':

        human_del = request.POST.get("list_to_delete").split()

        Birthday_boy.objects.filter(surname=human_del[0], name=human_del[1]).delete()
        story = f'{human_del[0]} {human_del[1]}  - УДАЛЁН'

        return render(request, 'reminders/index.html', context={'in_flag': in_flag, 'date_time': date_time,
                                                                'story': story})


    else:

        return render(request, 'reminders/delete.html',
                      context={'in_flag': in_flag, 'birthday': birthday})


def change(request):
    in_flag = True

    birthday = Birthday_boy.objects.filter(user=user_cod_id[0])
    count = Birthday_boy.objects.filter(user=user_cod_id[0]).count()

    return render(request, 'reminders/projects.html',
                  context={'in_flag': in_flag, 'birthday': birthday, 'count': count})

