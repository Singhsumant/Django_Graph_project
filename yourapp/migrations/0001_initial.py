# Generated by Django 5.0.1 on 2024-01-22 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='schoolModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=50)),
                ('language', models.CharField(max_length=50)),
            ],
        ),
    ]
