# Generated by Django 3.1.1 on 2023-05-16 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_hospitalservice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hospital',
            name='services',
        ),
    ]
