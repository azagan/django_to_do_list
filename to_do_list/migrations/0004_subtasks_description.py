# Generated by Django 3.2.4 on 2021-06-28 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0003_auto_20210624_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='subtasks',
            name='description',
            field=models.CharField(blank=True, max_length=255, verbose_name='Описание'),
        ),
    ]