from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

# Create your models here.

from django.db import models


class News(models.Model):
    title = models.CharField(max_length=200)  # Yangilik sarlavhasi
    content = models.TextField()  # To'liq yangilik matni
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)  # Yangilik rasmi
    created_at = models.DateTimeField(auto_now_add=True)  # Yaratilgan sana

    def __str__(self):
        return self.title


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


#class Teachers(models.Model):
#    name = models.CharField(max_length=55)
#    position = models.CharField(max_length=30)
#    phone = models.CharField(max_length=17, default='+998')
#    working_time = models.IntegerField(blank=True)
#    level = models.CharField(max_length=15, default="bo'sh", blank=True)
#    photo = models.ImageField(default="/media/about1.jpg", upload_to='images/', blank=True)
#    author = models.ForeignKey(
#        get_user_model(),
#        on_delete=models.CASCADE,
#    )
#
#    def __str__(self):
#        return self.name
#
#    def get_absolute_url(self):
#        return reverse('teachers_detail', args=[str(self.id)])
#
#
#class Students(models.Model):
#    name = models.CharField(max_length=55)
#    class_id = models.IntegerField()
#    class_letter = models.CharField(blank=True, max_length=1)
#    name_father = models.CharField(max_length=55)
#    name_mom = models.CharField(max_length=55)
#    phone_father = models.CharField(max_length=17, default='+998')
#    phone_mom = models.CharField(max_length=17, default='+998')
#    photo = models.ImageField(default="/media/about1.jpg", upload_to='images/', blank=True)
#    author = models.ForeignKey(
#        get_user_model(),
#        on_delete=models.CASCADE,
#    )
#
#    def __str__(self):
#        return self.name
#
#    def get_absolute_url(self):
#        return reverse('students_detail', args=[str(self.id)])
#

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

#
#class Students(models.Model):
#    name = models.CharField(max_length=55)
#    class_id = models.IntegerField()
#    class_letter = models.CharField(blank=True, max_length=1)
#    name_father = models.CharField(max_length=55)
#    name_mom = models.CharField(max_length=55)
#    phone_father = models.CharField(max_length=17, default='+998')
#    phone_mom = models.CharField(max_length=17, default='+998')
#    photo = models.ImageField(default="/media/about1.jpg", upload_to='images/', blank=True)
#    author = models.ForeignKey(
#        get_user_model(),
#        on_delete=models.CASCADE,
#    )
#    class_head = models.ForeignKey(
#        Teachers,
#        on_delete=models.SET_NULL,
#        null=True,
#        blank=True,
#        related_name='students',
#        verbose_name='Sinf Rahbari'
#    )
#
#    def __str__(self):
#        return self.name
#
#    def get_absolute_url(self):
#        return reverse('students_detail', args=[str(self.id)])


#  Sinfni alohida class qilib tayyorlangan moduli

class ClassName(models.Model):
    name = models.CharField(max_length=3, unique=True, verbose_name="Sinf Nomi")
    class_id = models.IntegerField()
    class_letter = models.CharField(blank=True, max_length=1)
    class_teacher = models.ForeignKey(
        'Teachers',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='class_groups',
        verbose_name='Sinf Rahbari'
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('class_name_detail', args=[str(self.id)])


class Students(models.Model):
    name = models.CharField(max_length=55)
    class_name = models.ForeignKey(
        ClassName,
        on_delete=models.CASCADE,
        related_name='students',
        verbose_name='Sinf'
    )
    name_father = models.CharField(max_length=55, verbose_name="Otasining ismi")
    name_mom = models.CharField(max_length=55, verbose_name="Onasining ismi")
    phone_father = models.CharField(max_length=17, default='+998', verbose_name="Otasi telefon raqami")
    phone_mom = models.CharField(max_length=17, default='+998', verbose_name="Onasi telefon raqami")
    photo = models.ImageField(default="/media/about1.jpg", upload_to='images/', blank=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('students_detail', args=[str(self.id)])