# Generated by Django 4.0.1 on 2022-02-03 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='email',
            field=models.CharField(max_length=200, null=True, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='data',
            name='created_at',
            field=models.FloatField(default=1643887360.195632),
        ),
    ]