from django.test import TestCase
from mixer.backend.django import mixer

from .models import Birthday_boy, Reminder, Day, Month


class BirthdayTestCaseMixer(TestCase):
    def setUp(self):
        self.birthday = mixer.blend(Birthday_boy)

        # day = mixer.blend(Day, day=2)
        # month = mixer.blend(Month, month='test_month')
        # self.birthday_str = mixer.blend(Birthday_boy, name='test_name', surname='test_surname', day=day, month=month)

        self.birthday_str = mixer.blend(Birthday_boy, name='test_name', surname='test_surname', day__day=2,
                                        month__month='test_month')

    def test_str(self):
        self.assertEqual(str(self.birthday_str), 'test_surname test_name   (2 : test_month)')


class ReminderTestCaseMixer(TestCase):
    def setUp(self):
        self.reminder = mixer.blend(Reminder)

        self.reminder_str = mixer.blend(Reminder, reminder='test_text', day__day=1, month__month='test_month')

    def test_str(self):
        self.assertEqual(str(self.reminder_str), '[  test_text  ] - напомнить - (1 : test_month)')
