# Generated by Django 4.1.3 on 2023-02-28 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=256, verbose_name='Название навыка')),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=210, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=210, verbose_name='Фамилия')),
                ('age', models.IntegerField(verbose_name='Возраст')),
                ('student_class', models.IntegerField(verbose_name='Класс')),
            ],
        ),
    ]
