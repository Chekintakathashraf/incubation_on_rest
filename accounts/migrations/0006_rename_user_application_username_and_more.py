# Generated by Django 4.1 on 2022-09-03 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_slots'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='user',
            new_name='username',
        ),
        migrations.RenameField(
            model_name='slots',
            old_name='companyname',
            new_name='company_name',
        ),
    ]
