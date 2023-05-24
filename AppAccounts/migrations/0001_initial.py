# Generated by Django 4.1 on 2023-05-24 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('skill', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('biography', models.TextField()),
                ('images', models.ImageField(upload_to='')),
            ],
        ),
    ]
