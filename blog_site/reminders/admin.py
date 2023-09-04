from django.contrib import admin
from .models import Day,Month, Birthday_boy, Reminder

admin.site.register(Birthday_boy)
admin.site.register(Day)
admin.site.register(Month)
admin.site.register(Reminder)
