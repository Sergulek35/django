from django.contrib import admin
from .models import Day,Month, Birthday_boy, User

admin.site.register(Birthday_boy)
admin.site.register(Day)
admin.site.register(Month)
admin.site.register(User)
