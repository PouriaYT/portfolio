# Generated by Django 4.0.1 on 2022-02-03 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام و نام خانوادگی')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان')),
                ('phone_number', models.CharField(max_length=200, verbose_name='شماره تماس')),
                ('created_at', models.FloatField(default=1643884700.573344)),
            ],
        ),
    ]
