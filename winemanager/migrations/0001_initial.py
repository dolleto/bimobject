# Generated by Django 5.1.4 on 2024-12-12 10:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Winemaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='WineBottle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('year', models.PositiveIntegerField()),
                ('size', models.CharField(max_length=50)),
                ('count_in_winecellar', models.PositiveIntegerField()),
                ('style', models.CharField(choices=[('dry', 'Dry'), ('sweet', 'Sweet')], max_length=50)),
                ('taste', models.TextField(help_text='Comma separated, e.g., plum, tobacco')),
                ('description', models.TextField()),
                ('food_pairing', models.TextField()),
                ('link', models.URLField(blank=True, null=True)),
                ('winemaker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wines', to='winemanager.winemaker')),
            ],
        ),
    ]
