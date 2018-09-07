# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-13 17:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Design',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Название пункта')),
                ('text', models.TextField(max_length=500, verbose_name='Текст')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Вид Проектирования',
                'verbose_name_plural': 'Виды Проектирования',
            },
        ),
        migrations.CreateModel(
            name='Expertise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Название файла')),
                ('file', models.FileField(upload_to='', verbose_name='Файл')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Файл',
                'verbose_name_plural': 'Файлы',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=200, verbose_name='Название новости')),
                ('image', models.ImageField(upload_to='images/news/', verbose_name='Картинка новости')),
                ('text', models.TextField(verbose_name='Текст для новости')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.CreateModel(
            name='Photos_for_Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, verbose_name='Название подборки фоток')),
                ('title', models.CharField(blank=True, max_length=250, verbose_name='Заголовок для фоток')),
                ('images', models.ImageField(upload_to='images/portfolio/', verbose_name='фото для портфолио')),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='design', to='ndi_app.Design', verbose_name='Вид проектирования')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Фото Портфолио',
                'verbose_name_plural': 'Фотки портфолио',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, verbose_name='Название слайда')),
                ('text', models.CharField(blank=True, max_length=500, verbose_name='Текст слайда')),
                ('image', models.ImageField(upload_to='images/slider/', verbose_name='Картинка слайдера')),
                ('link', models.URLField()),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Слайдер',
                'verbose_name_plural': 'Слайды',
            },
        ),
    ]
