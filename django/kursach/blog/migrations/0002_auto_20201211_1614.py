# Generated by Django 3.1.2 on 2020-12-11 13:14

import blog.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'verbose_name': 'Блог', 'verbose_name_plural': 'Блог'},
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('body', models.TextField(max_length=5000, verbose_name='Сообщение')),
                ('image', models.ImageField(upload_to=blog.models.upload_location, verbose_name='Картинка')),
                ('document', models.FileField(upload_to='documents/', verbose_name='файл')),
                ('date_published', models.DateField(auto_now_add=True, verbose_name='Дата публикации')),
                ('date_update', models.DateField(auto_now=True, verbose_name='Дата изменения')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Программа',
                'verbose_name_plural': 'Программа',
            },
        ),
    ]
