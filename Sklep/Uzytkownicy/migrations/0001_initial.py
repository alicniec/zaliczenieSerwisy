# Generated by Django 3.2.9 on 2022-01-13 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Klient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=30)),
                ('nazwisko', models.CharField(max_length=30)),
                ('username', models.CharField(db_index=True, max_length=255, unique=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('haslo', models.CharField(max_length=255)),
                ('telefon', models.CharField(max_length=11)),
                ('data_utworzenia', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'Klient',
                'verbose_name_plural': 'Klienci',
                'ordering': ['username'],
            },
        ),
    ]