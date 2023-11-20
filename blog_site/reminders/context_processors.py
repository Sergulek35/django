from django.core.exceptions import ObjectDoesNotExist

from reminders.models import Birthday_boy


def name_bot(request):
    return {"name_bot": 'TummyBot'}


def story(request):
    try:
        story = Birthday_boy.objects .filter(user = request.user).latest('id')
        return {"story": story}
    except TypeError:
        return {"story": ''}
    except ObjectDoesNotExist:
        return {"story": ''}