# Generated by Django 2.1.9 on 2019-06-24 07:57

from django.db import migrations, models

def mergeDepartments(apps, schema_editor):
    Room = apps.get_model('base', 'Room')
    RoomType = apps.get_model('base', 'RoomType')

    room_departments = set()     
    for type in RoomType.objects.all(): 
        for room in Room.objects.filter(subroom_of__types = type):
            room_departments.add((room, type.department)) 
    
    for room, department in room_departments:
        room.departments.add(department)


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0033_timegeneralsettings_default_preference_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='departments',
            field=models.ManyToManyField(to='base.Department'),
        ),
        migrations.RunPython(mergeDepartments),
    ]
