# Generated by Django 3.0.8 on 2021-02-04 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_aboutus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutus',
            name='paragraph',
        ),
        migrations.RemoveField(
            model_name='aboutus',
            name='titel',
        ),
    ]
