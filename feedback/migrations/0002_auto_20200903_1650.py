# Generated by Django 3.0.8 on 2020-09-03 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedback',
            options={'verbose_name': 'обратная связь', 'verbose_name_plural': 'отзывы'},
        ),
    ]