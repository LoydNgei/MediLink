# Generated by Django 3.1.1 on 2023-05-18 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0033_hospital_home_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='description',
            field=models.TextField(blank=True, default="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries", max_length=500),
        ),
    ]
