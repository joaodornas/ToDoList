# Generated by Django 3.1.1 on 2020-09-02 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoList', '0004_auto_20200902_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='user_id',
            field=models.IntegerField(default=0),
        ),
    ]
