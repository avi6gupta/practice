# Generated by Django 2.1 on 2018-08-08 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='people',
            name='img',
        ),
    ]
