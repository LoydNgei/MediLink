# Generated by Django 3.1.1 on 2023-05-16 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_auto_20230516_2300'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(max_length=100)),
                ('service', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='hospital',
            name='accepted_paymentservices',
            field=models.ManyToManyField(to='store.PaymentService'),
        ),
    ]
