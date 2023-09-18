# Generated by Django 3.2.7 on 2023-08-08 05:48

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(max_length=255, upload_to='')),
                ('title', models.CharField(max_length=255)),
                ('min_description', models.CharField(max_length=255)),
                ('description', tinymce.models.HTMLField()),
            ],
            options={
                'db_table': 'Courses',
            },
        ),
    ]