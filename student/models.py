from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

# Create your models here.


class Workers(models.Model):
    name = models.CharField(max_length=55)
    position = models.CharField(max_length=30)
    phone = models.CharField(max_length=17, default='+998')
    photo = models.ImageField(default="/media/about1.jpg", upload_to='images/', blank=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('workers_detail', args=[str(self.id)])


class Teachers(models.Model):
    name = models.CharField(max_length=55)
    position = models.CharField(max_length=30)
    phone = models.CharField(max_length=17, default='+998')
    working_time = models.IntegerField(blank=True)
    level = models.CharField(max_length=15, default="bo'sh", blank=True)
    photo = models.ImageField(default="/media/about1.jpg", upload_to='images/', blank=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('teachers_detail', args=[str(self.id)])


class Students(models.Model):
    name = models.CharField(max_length=55)
    class_id = models.IntegerField()
    class_letter = models.CharField(blank=True, max_length=1)
    name_father = models.CharField(max_length=55)
    name_mom = models.CharField(max_length=55)
    phone_father = models.CharField(max_length=17, default='+998')
    phone_mom = models.CharField(max_length=17, default='+998')
    photo = models.ImageField(default="/media/about1.jpg", upload_to='images/', blank=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('students_detail', args=[str(self.id)])