# Generated by Django 5.0.7 on 2024-07-19 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_name', models.CharField(max_length=30)),
                ('stu_city', models.CharField(max_length=30)),
                ('stu_email', models.EmailField(max_length=254)),
            ],
            options={
                'db_table': 'Student',
            },
        ),
    ]
