# Generated by Django 3.0.14 on 2022-07-16 20:00

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0088_courseadditional_over_time'),
        ('TTapp', '0061_respectminhoursperday'),
    ]

    operations = [
        migrations.CreateModel(
            name='LimitCourseTypeTimePerPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.PositiveSmallIntegerField(blank=True, default=None, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(8)])),
                ('title', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('comment', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active?')),
                ('modified_at', models.DateField(auto_now=True)),
                ('max_hours', models.PositiveSmallIntegerField()),
                ('period', models.CharField(choices=[('fd', 'Full day'), ('hd', 'Half day')], max_length=2)),
                ('course_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.CourseType')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Department')),
                ('train_progs', models.ManyToManyField(blank=True, to='base.TrainingProgramme')),
                ('weeks', models.ManyToManyField(blank=True, to='base.Week')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]