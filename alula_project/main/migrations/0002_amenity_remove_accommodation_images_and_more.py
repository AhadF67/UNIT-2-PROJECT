# Generated by Django 5.0.6 on 2024-07-16 08:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='accommodation',
            name='images',
        ),
        migrations.RemoveField(
            model_name='accommodation',
            name='amenities',
        ),
        migrations.CreateModel(
            name='AccommodationImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='accommodation_images')),
                ('accommodation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main.accommodation')),
            ],
        ),
        migrations.AddField(
            model_name='accommodation',
            name='amenities',
            field=models.ManyToManyField(to='main.amenity'),
        ),
    ]