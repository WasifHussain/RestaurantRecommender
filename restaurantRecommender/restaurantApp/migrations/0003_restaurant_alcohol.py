# Generated by Django 4.0.3 on 2022-04-07 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantApp', '0002_alter_restaurant_accessibility_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='alcohol',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]