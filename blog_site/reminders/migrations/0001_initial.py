# Generated by Django 4.1.7 on 2023-04-10 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Month',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Birthday_boy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='default name', max_length=32)),
                ('surname', models.CharField(max_length=32, unique=True)),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reminders.day')),
                ('month', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reminders.month')),
            ],
        ),
    ]