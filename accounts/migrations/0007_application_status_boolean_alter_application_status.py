# Generated by Django 4.1 on 2022-09-03 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_rename_user_application_username_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='status_boolean',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('Registration_pending', 'Registration_pending'), ('Registration_approved ', 'Registration_approved'), ('Registration_rejected', 'Registration_rejected')], default='Registration_pending', max_length=100),
        ),
    ]
