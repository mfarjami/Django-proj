# Generated by Django 3.2.7 on 2021-10-09 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='body',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]
