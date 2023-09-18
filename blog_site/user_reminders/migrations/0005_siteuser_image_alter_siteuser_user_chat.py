# Generated by Django 4.1.7 on 2023-08-28 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_reminders', '0004_alter_siteuser_is_author_alter_siteuser_user_chat'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteuser',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='avatar'),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='user_chat',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]
