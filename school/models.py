from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.


class HomePhoto1(models.Model):
    name = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=250, blank=True)
    photo = models.ImageField(upload_to='images/display/')
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )


class HomePhotoUniform(models.Model):
    detail = models.CharField(max_length=300)
    photo = models.ImageField(upload_to='images/display/')
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )


class HomePhotoRoom(models.Model):
    name = models.CharField(max_length=100)
    detail = models.TextField(default=True)
    photo = models.ImageField(upload_to='images/display/')
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )


class HomeBlog(models.Model):
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='images/display/')
    detail = models.TextField()
    data = models.DateTimeField()
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )


class AboutName(models.Model):
    name = models.CharField(max_length=90)
    detail = models.TextField()
    advantages = models.TextField()


class AboutStaff(models.Model):
    photo = models.ImageField(upload_to='images/display/')
    name = models.CharField(max_length=90)
    staff = models.CharField(max_length=70)
    level = models.CharField(max_length=150)


class YouTubeVideo(models.Model): # About saxifasidagi videoning moduli
    title = models.CharField(max_length=200) # Videoning tepasidagi yozuvi
    video_url = models.URLField()  # YouTube video URL-ni saqlash uchun
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


#class AboutVideos(models.Model):
#    name = models.CharField(max_length=255)  # Video nomi
#    video_url = models.URLField(default=True)  # YouTube video havolasi
#    time = models.DateTimeField(auto_now_add=True)  # Qo'shilgan vaqti
#
#    def __str__(self):
#        return self.name
#
#    def embed_url(self):
#        # YouTube havolasidan video ID'sini ajratish va embed formatga o'tkazish
#        video_id = self.video_url.split('v=')[-1]
#        return f"https://www.youtube.com/embed/{video_id}"


class AboutGallery(models.Model):
    name = models.CharField(max_length=40)
    photo = models.ImageField(upload_to='images/display/')


class ContactAddress(models.Model):
    address = models.CharField(max_length=255, verbose_name="Manzil")
    phone = models.CharField(max_length=20, verbose_name="Telefon raqami")
    email = models.EmailField(verbose_name="Email")
    fax = models.CharField(max_length=20, verbose_name="Faks")
    telegram = models.CharField(max_length=50, verbose_name="Telegram", blank=True, null=True)
    facebook = models.CharField(max_length=50, verbose_name="Facebook", blank=True, null=True)

    def __str__(self):
        return self.address


class ContactMap(models.Model):
    title = models.CharField(max_length=200)
    map_url = models.URLField()  # Xaritadagi joylashuv URL-ni saqlash uchun
    added_date = models.DateTimeField(auto_now_add=True)


class LessonTable(models.Model):
    name = models.CharField(max_length=50)
    grade = models.IntegerField()
    letter = models.CharField(max_length=1)
    photo = models.ImageField(upload_to='images/display/')

    def save(self, *args, **kwargs):
        if 1 <= self.grade <= 11:
            super(LessonTable, self).save(*args, **kwargs)
        else:
            raise ValueError("Raqam 1-11 oralig'ida bo'lishi kerak!")

    def __str__(self):
        return str(self.grade)


class TableTime(models.Model):
    name = models.CharField(max_length=80)
    photo = models.ImageField(upload_to='images/display/')


class LogoFoto(models.Model):
    name = models.CharField(max_length=80)
    photo = models.ImageField(upload_to='images/display/')


class Contact(models.Model):
    phone_number = models.CharField(max_length=13, default='+998', null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    facebook_address = models.URLField(null=True, blank=True)
    youtube_address = models.URLField(null=True, blank=True)
    telegram_channel_address = models.URLField(null=True, blank=True)
    instagram_address = models.URLField(null=True, blank=True)
    telegram_bot_address = models.URLField(null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)

