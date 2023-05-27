# Generated by Django 3.0.5 on 2021-04-26 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0072_coursemodification_room_old_is_visio'),
        ('TTapp', '0042_auto_20210301_2100')
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursemodification',
            name='room_old_is_visio',
        ),
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='group',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.GroupType'),
        ),
        migrations.AlterField(
            model_name='module',
            name='abbrev',
            field=models.CharField(max_length=100, verbose_name='Abbreviation'),
        ),
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='trainingprogramme',
            name='abbrev',
            field=models.CharField(max_length=50),
        ),
    ]
