# Generated by Django 3.2.7 on 2023-08-10 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_coursesdetails_video_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursesdetails',
            name='video_link',
            field=models.TextField(),
        ),
    ]
