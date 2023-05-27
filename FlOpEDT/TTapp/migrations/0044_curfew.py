# Generated by Django 3.0.5 on 2021-04-29 14:32

import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0073_auto_20210426_1544'),
        ('TTapp', '0043_auto_20210329_1452'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curfew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.PositiveSmallIntegerField(blank=True, default=None, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(52)])),
                ('year', models.PositiveSmallIntegerField(blank=True, default=None, null=True)),
                ('weight', models.PositiveSmallIntegerField(blank=True, default=None, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(8)])),
                ('comment', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Contrainte active?')),
                ('weekdays', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('m', 'monday'), ('tu', 'tuesday'), ('w', 'wednesday'), ('th', 'thursday'), ('f', 'friday'), ('sa', 'saturday'), ('su', 'sunday')], max_length=2), blank=True, null=True, size=None)),
                ('curfew_time', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(1440)])),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Department')),
                ('train_progs', models.ManyToManyField(blank=True, to='base.TrainingProgramme')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]