# Generated by Django 3.0.8 on 2021-02-04 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20210204_1750'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aboutusparag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paragraph', models.CharField(max_length=20000)),
            ],
        ),
    ]