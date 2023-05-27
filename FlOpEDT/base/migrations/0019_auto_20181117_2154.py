# Generated by Django 2.1.3 on 2018-11-17 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_auto_20181117_2138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursemodification',
            name='creneau_old',
        ),
        migrations.RemoveField(
            model_name='scheduledcourse',
            name='tday',
        ),
        migrations.AlterField(
            model_name='coursemodification',
            name='day_old',
            field=models.CharField(choices=[('m', 'monday'), ('tu', 'tuesday'), ('w', 'wednesday'), ('th', 'thursday'), ('f', 'friday'), ('sa', 'saturday'), ('su', 'sunday')], default=None, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='coursemodification',
            name='start_time_old',
            field=models.PositiveSmallIntegerField(default=None, null=True),
        ),
    ]