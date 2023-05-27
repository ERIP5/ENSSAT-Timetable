# Generated by Django 2.1.7 on 2019-04-23 09:01

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_auto_20190120_1719'),
        ('people', '0007_auto_20190311_1920'),
        ('TTapp', '0009_auto_20190116_1031'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomConstraint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.PositiveSmallIntegerField(blank=True, default=None, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(52)])),
                ('year', models.PositiveSmallIntegerField(blank=True, default=None, null=True)),
                ('weight', models.PositiveSmallIntegerField(blank=True, default=None, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(8)])),
                ('comment', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Contrainte active?')),
                ('class_name', models.CharField(default=None, max_length=200)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Department')),
                ('groups', models.ManyToManyField(blank=True, to='base.Group')),
                ('modules', models.ManyToManyField(blank=True, to='base.Module')),
                ('train_prog', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.TrainingProgramme')),
                ('tutors', models.ManyToManyField(blank=True, to='people.Tutor')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]