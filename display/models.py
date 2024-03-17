#from django.contrib.auth import get_user_model
#from django.db import models
#
#
## Create your models here.
#
#
#class HomePhoto1(models.Model):
#    name = models.CharField(max_length=100, blank=True)
#    address = models.CharField(max_length=250, blank=True)
#    photo = models.ImageField(upload_to='images/')
#    author = models.ForeignKey(
#        get_user_model(),
#        on_delete=models.CASCADE,
#    )
#
#
#class HomePhotoUniform(models.Model):
#    detail = models.CharField(max_length=300)
#    photo = models.ImageField(upload_to='images/')
#    author = models.ForeignKey(
#        get_user_model(),
#        on_delete=models.CASCADE,
#    )
#
#
#class HomePhotoRoom(models.Model):
#    name = models.CharField(max_length=100)
#    detail = models.TextField(default=True)
#    photo = models.ImageField()
#    author = models.ForeignKey(
#        get_user_model(),
#        on_delete=models.CASCADE,
#    )
#
#
#class HomeBlog(models.Model):
#    name = models.CharField(max_length=200)
#    short_name = models.CharField(max_length=20)
#    photo = models.ImageField(upload_to='images/')
#    detail = models.TextField()
#    data = models.DateTimeField()
#    author = models.ForeignKey(
#        get_user_model(),
#        on_delete=models.CASCADE,
#    )
#
#
#class AboutName(models.Model):
#    name = models.CharField(max_length=90)
#    detail = models.TextField()
#    advantages = models.TextField()
#
#
#class AboutStaff(models.Model):
#    photo = models.ImageField(upload_to='images/')
#    name = models.CharField(max_length=90)
#    staff = models.CharField(max_length=70)
#    level = models.CharField(max_length=150)
#
#
#class AboutVideos(models.Model):
#    name = models.CharField(max_length=255)
#    video = models.FileField(upload_to='videos/')
#    time = models.DateTimeField(auto_now_add=True)
#
#    def __str__(self):
#        return self.name
#
#
#class AboutGallery(models.Model):
#    name = models.CharField(max_length=40)
#    photo = models.ImageField(upload_to='images/')
#
#
#class ContactAddress(models.Model):
#    pass
#    #name = models.CharField(max_length=255)
#
#
#class ContactMap(models.Model):
#    pass
#    #name = models.CharField(max_length=255)
#
#







