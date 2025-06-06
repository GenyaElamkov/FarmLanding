# Generated by Django 5.2.2 on 2025-06-06 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lending', '0010_rename_grade_review_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Заголовок')),
                ('description', models.TextField(blank=True, max_length=500, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='hero')),
            ],
            options={
                'verbose_name': 'Гланая',
                'verbose_name_plural': 'Главная',
            },
        ),
    ]
