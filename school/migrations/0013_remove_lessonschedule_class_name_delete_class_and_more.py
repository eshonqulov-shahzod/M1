# Generated by Django 5.0.1 on 2024-11-10 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0012_class_lessonschedule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lessonschedule',
            name='class_name',
        ),
        migrations.DeleteModel(
            name='Class',
        ),
        migrations.DeleteModel(
            name='LessonSchedule',
        ),
    ]
