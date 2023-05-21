# Generated by Django 3.1.1 on 2023-05-17 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0021_hospital_service_provided'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('specialty', models.CharField(max_length=100)),
                ('available_from', models.DateField()),
                ('available_to', models.DateField()),
                ('hospitals_worked', models.ManyToManyField(related_name='doctors', to='store.Hospital')),
            ],
        ),
    ]