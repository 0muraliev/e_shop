# Generated by Django 3.0.8 on 2020-08-27 10:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=85, null=True, verbose_name='Ваше имя')),
                ('email', models.EmailField(max_length=254, verbose_name='Ваша электронная почта')),
                ('topic', models.CharField(max_length=55, verbose_name='Тема')),
                ('text', models.TextField(verbose_name='Подробнее')),
                ('image', models.ImageField(blank=True, null=True, upload_to='feedback', verbose_name='Приложить фотографию (рекомендуется)')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата обращения')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Обратная связь',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]