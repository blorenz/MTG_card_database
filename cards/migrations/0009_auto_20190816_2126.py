# Generated by Django 2.2 on 2019-08-16 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0008_auto_20190816_2107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='Name',
        ),
        migrations.AddField(
            model_name='card',
            name='abitities',
            field=models.CharField(default=True, max_length=120),
        ),
        migrations.AddField(
            model_name='card',
            name='artist',
            field=models.CharField(default=True, max_length=120),
        ),
        migrations.AddField(
            model_name='card',
            name='card_number',
            field=models.CharField(default=True, max_length=120),
        ),
        migrations.AddField(
            model_name='card',
            name='flavor_text',
            field=models.TextField(default=True),
        ),
        migrations.AddField(
            model_name='card',
            name='name',
            field=models.CharField(default=True, max_length=120),
        ),
        migrations.AddField(
            model_name='card',
            name='text',
            field=models.TextField(default=True),
        ),
    ]
