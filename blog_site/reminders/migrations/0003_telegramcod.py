# Generated by Django 4.1.7 on 2023-08-28 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminders', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramCod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_cod', models.PositiveIntegerField(unique=True)),
            ],
        ),
    ]
