# Generated by Django 4.2.5 on 2023-09-30 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_alter_todo_date_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='date_created',
        ),
    ]
