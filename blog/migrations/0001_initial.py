# Generated by Django 4.2 on 2024-10-31 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('content', models.TextField(verbose_name='Контент')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='blog/')),
                ('is_active', models.BooleanField(default=True)),
                ('number_of_views', models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')),
                ('date_of_publication', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Блог',
                'verbose_name_plural': 'Блоги',
            },
        ),
    ]
