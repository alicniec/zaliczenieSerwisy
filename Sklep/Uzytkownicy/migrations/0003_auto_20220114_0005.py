# Generated by Django 3.2.9 on 2022-01-13 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Uzytkownicy', '0002_auto_20220113_2347'),
    ]

    operations = [
        migrations.AddField(
            model_name='uzytkownik',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='uzytkownik',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
