# Generated by Django 3.2.7 on 2023-08-30 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_coursesdetails_courses'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(max_length=1000)),
                ('timestamp', models.DateField(auto_now=True)),
                ('commentid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.coursesdetails')),
            ],
            options={
                'db_table': 'Comments',
            },
        ),
    ]