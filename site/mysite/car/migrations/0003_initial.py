# Generated by Django 4.2.1 on 2023-06-07 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('car', '0002_delete_car'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('edesc', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('erem', models.BooleanField(default=False, verbose_name='Удалить?')),
                ('name', models.CharField(default='Машинка', max_length=255, verbose_name='Название')),
                ('color', models.CharField(default='Черный', max_length=255, verbose_name='Цвет')),
                ('nomb', models.CharField(default='TO123P', max_length=255, verbose_name='Номер')),
            ],
            options={
                'verbose_name': 'Машинка',
                'verbose_name_plural': 'Машинки',
                'ordering': ['id'],
            },
        ),
    ]
