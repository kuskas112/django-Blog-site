# Generated by Django 4.1.7 on 2023-07-08 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='photo',
        ),
    ]
