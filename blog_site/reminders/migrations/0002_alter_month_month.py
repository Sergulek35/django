# Generated by Django 4.1.7 on 2023-04-10 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='month',
            name='month',
            field=models.CharField(max_length=12, unique=True),
        ),
    ]
