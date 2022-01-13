# Generated by Django 3.2.10 on 2022-01-11 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Produkty', '0004_produkty_gatunek'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Kategoria',
                'verbose_name_plural': 'Kategorie',
            },
        ),
        migrations.AddField(
            model_name='produkty',
            name='kategoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Produkty.kategoria'),
        ),
    ]