# Generated by Django 5.0.3 on 2024-03-04 17:10
from django.conf import settings
from django.db import migrations, models


def add_client_categories(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    ClientCategory = apps.get_model('client', 'ClientCategory')
    client_categories_list = []
    path_to_json = f'{settings.BASE_DIR}/apps/client/management/commands/files/dataset.txt'
    with open(path_to_json, encoding='utf-8') as dataset_file:
        for data in dataset_file.readlines()[1:]:
            list_data = data.split(',')
            client_categories_list.append(
                ClientCategory(
                    category=list_data[0],
                    first_name=list_data[1],
                    last_name=list_data[2],
                    email=list_data[3],
                    gender=list_data[4],
                    birth_date=list_data[5],
                )
            )
        ClientCategory.objects.using(db_alias).bulk_create(client_categories_list)


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, default='', help_text='Категорія', max_length=255)),
                ('email', models.EmailField(blank=True, default='', help_text='Електронна пошта', max_length=255)),
                ('first_name', models.CharField(blank=True, default='', help_text='Імʼя', max_length=100)),
                ('last_name', models.CharField(blank=True, default='', help_text='Прізвище', max_length=100)),
                ('birth_date', models.DateField(blank=True, help_text='Дата народження', null=True)),
                ('gender', models.CharField(choices=[('male', 'Чоловік'), ('female', 'Жінка')], default='male', help_text='Стать', max_length=100)),
            ],
            options={
                'verbose_name': 'Категорія клієнта',
                'verbose_name_plural': 'Категорії клієнта',
                'ordering': ['-id'],
            },
        ),
        migrations.RunPython(add_client_categories, reverse_code=migrations.RunPython.noop),
    ]