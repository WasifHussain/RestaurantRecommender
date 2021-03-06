# Generated by Django 4.0.3 on 2022-04-07 14:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField(max_length=100)),
                ('city', models.TextField(max_length=50)),
                ('smoking_area', models.TextField(blank=True, null=True)),
                ('dresscode', models.TextField(blank=True, null=True)),
                ('accessibility', models.TextField(blank=True, null=True)),
                ('price', models.CharField(max_length=10)),
                ('ambience', models.CharField(blank=True, max_length=10, null=True)),
                ('area', models.CharField(blank=True, max_length=10, null=True)),
                ('other_services', models.CharField(blank=True, max_length=100, null=True)),
                ('favorite', models.ManyToManyField(related_name='favorite', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
