# Generated by Django 3.1.1 on 2020-09-02 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoList', '0003_remove_task_task_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='username',
            new_name='user_id',
        ),
    ]