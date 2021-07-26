# Generated by Django 3.0.8 on 2021-01-28 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_masterchef'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='info/%Y/%m/%d/')),
                ('title', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
    ]