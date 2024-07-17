# Generated by Django 5.0.6 on 2024-07-17 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_dining_images_diningimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dining',
            name='menu',
        ),
        migrations.AddField(
            model_name='dining',
            name='category',
            field=models.CharField(default='Fine dining', max_length=100),
        ),
        migrations.AddField(
            model_name='dining',
            name='dress',
            field=models.CharField(default='casual', max_length=100),
        ),
        migrations.AddField(
            model_name='dining',
            name='price',
            field=models.CharField(default='$$', max_length=100),
        ),
    ]
