# Generated by Django 3.0.8 on 2021-02-03 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_statement_titelrls'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Statement',
            new_name='Rules',
        ),
        migrations.RenameModel(
            old_name='Titelrls',
            new_name='Titelrules',
        ),
        migrations.RenameField(
            model_name='rules',
            old_name='paragraph',
            new_name='statement',
        ),
    ]