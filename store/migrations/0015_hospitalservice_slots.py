# Generated by Django 3.1.1 on 2023-05-16 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_hospitalservice_availability'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospitalservice',
            name='slots',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
