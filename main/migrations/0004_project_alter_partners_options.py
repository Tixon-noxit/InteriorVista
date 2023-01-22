# Generated by Django 4.0.3 on 2022-07-26 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_partners'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название проекта')),
                ('Preview', models.ImageField(upload_to='', verbose_name='Преью')),
                ('Photos1', models.ImageField(blank=True, upload_to='', verbose_name='Фото 1')),
                ('Photos2', models.ImageField(blank=True, upload_to='', verbose_name='Фото 2')),
                ('Photos3', models.ImageField(blank=True, upload_to='', verbose_name='Фото 3')),
                ('Photos4', models.ImageField(blank=True, upload_to='', verbose_name='Фото 4')),
                ('Photos5', models.ImageField(blank=True, upload_to='', verbose_name='Фото 5')),
                ('Photos6', models.ImageField(blank=True, upload_to='', verbose_name='Фото 6')),
                ('Photos7', models.ImageField(blank=True, upload_to='', verbose_name='Фото 7')),
                ('Photos8', models.ImageField(blank=True, upload_to='', verbose_name='Фото 8')),
                ('Photos9', models.ImageField(blank=True, upload_to='', verbose_name='Фото 9')),
                ('Photos10', models.ImageField(blank=True, upload_to='', verbose_name='Фото 10')),
                ('linkVK', models.CharField(blank=True, max_length=50, verbose_name='VK')),
                ('linkTwitter', models.CharField(blank=True, max_length=50, verbose_name='Twitter')),
                ('linkInstagram', models.CharField(blank=True, max_length=50, verbose_name='Instagram')),
                ('linkRarible', models.CharField(blank=True, max_length=50, verbose_name='Rarible')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
                'ordering': ['time_create', 'title'],
            },
        ),
        migrations.AlterModelOptions(
            name='partners',
            options={'verbose_name': 'Клиент', 'verbose_name_plural': 'Сотрудничество'},
        ),
    ]
