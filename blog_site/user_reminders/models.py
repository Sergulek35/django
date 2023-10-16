from django.db import models
from django.contrib.auth.models import AbstractUser


class SiteUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_author = models.BooleanField(default=False)
    user_chat = models.PositiveIntegerField(unique=True)
    image = models.ImageField(upload_to='avatar', null=True, blank=True)

    def __str__(self):
        return self.username


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not Profile.objects.filter(user=self).exists():
            Profile.objects.create(user=self)

class Profile(models.Model):
    info = models.TextField(blank=True)
    birth_date = models.DateField(null=True)
    user = models.OneToOneField(SiteUser, on_delete=models.CASCADE)

