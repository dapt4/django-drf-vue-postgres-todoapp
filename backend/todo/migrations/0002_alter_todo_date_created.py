# Generated by Django 4.2.5 on 2023-09-30 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date_created',
            field=models.DateTimeField(auto_created=True, auto_now=True),
        ),
    ]
