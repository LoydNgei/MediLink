# Generated by Django 3.1.1 on 2023-05-15 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_auto_20230515_0708'),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=200)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('location', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField()),
                ('services_offered', models.CharField(max_length=500)),
                ('pricing', models.CharField(max_length=200)),
                ('availability', models.CharField(max_length=200)),
                ('ratings', models.FloatField()),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('image', models.ImageField(upload_to='photos/products')),
                ('is_available', models.BooleanField(default=True)),
                ('home_general', models.BooleanField(default=False)),
                ('home_specialty', models.BooleanField(default=False)),
                ('home_psychiatric', models.BooleanField(default=False)),
                ('home_clinic', models.BooleanField(default=False)),
                ('affordable', models.BooleanField(default=False)),
                ('top_rated', models.BooleanField(default=False)),
                ('new', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
        ),
        migrations.CreateModel(
            name='MedicalStaff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('qualification', models.CharField(max_length=200)),
                ('specialty', models.CharField(max_length=200)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.hospital')),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
