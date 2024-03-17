# Generated by Django 5.0.1 on 2024-03-09 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_alter_aboutgallery_photo_alter_aboutstaff_photo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LessonTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('grade', models.IntegerField()),
                ('letter', models.CharField(max_length=1)),
                ('photo', models.ImageField(upload_to='images/display/')),
            ],
        ),
        migrations.CreateModel(
            name='TableTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('photo', models.ImageField(upload_to='images/display/')),
            ],
        ),
    ]