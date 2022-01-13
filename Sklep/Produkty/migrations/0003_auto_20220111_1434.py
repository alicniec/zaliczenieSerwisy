# Generated by Django 3.2.10 on 2022-01-11 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Produkty', '0002_rename_produty_produkty'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gatunki',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Gatunek',
                'verbose_name_plural': 'Gatunki',
            },
        ),
        migrations.AlterModelOptions(
            name='produkty',
            options={'verbose_name': 'Produkt', 'verbose_name_plural': 'Produkty'},
        ),
        migrations.RemoveField(
            model_name='produkty',
            name='gatunek',
        ),
    ]