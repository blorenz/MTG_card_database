# Generated by Django 2.2 on 2019-08-16 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0007_auto_20190815_2023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='Abitities',
        ),
        migrations.RemoveField(
            model_name='card',
            name='Artist',
        ),
        migrations.RemoveField(
            model_name='card',
            name='Card_Number',
        ),
        migrations.RemoveField(
            model_name='card',
            name='Flavor_text',
        ),
        migrations.RemoveField(
            model_name='card',
            name='Text',
        ),
    ]
