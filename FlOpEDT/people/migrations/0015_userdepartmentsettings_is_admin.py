# Generated by Django 2.1.3 on 2020-01-26 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0014_remove_fullstaff_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdepartmentsettings',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]
