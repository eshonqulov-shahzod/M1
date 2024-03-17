from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import TemplateView
from .models import (
    LogoFoto,
    Contact,
    HomePhoto1,
    HomeBlog,
    HomePhotoUniform,
    HomePhotoRoom,
    AboutName,
    AboutStaff,
    AboutGallery,
    AboutVideos,
    ContactMap,
    ContactAddress,
    TableTime,
    LessonTable,

    )


# Create your views here.


class IndexUrls(ListView):
    model = HomePhoto1
    template_name = 'index.html'
    context_object_name = 'homeobject'

    def get_queryset(self):
        return {
            'home_photo1': HomePhoto1.objects.order_by('-id')[:1],
            'home_blog': HomeBlog.objects.order_by('-id')[:5],
            'home_uniform': HomePhotoUniform.objects.all(),
            'home-room': HomePhotoRoom.objects.all(),
        }


class BlogUrls(ListView):
    model = HomeBlog
    template_name = 'blog.html'
    context_object_name = 'blogobject'

    def get_queryset(self):
        return {
            'blog': HomeBlog.objects.order_by('-id')[:18],
            'blog_full': HomeBlog.objects.order_by('-id')
        }


class AboutUsUrls(ListView):
    model = AboutName
    template_name = 'about-us.html'
    context_object_name = 'aboutobject'

    def get_queryset(self):
        return {
            'about_name': AboutName.objects.all(),
            'about_staff': AboutStaff.objects.order_by('-id')[:3],
            'about_gallery': AboutGallery.objects.order_by('-id')[:4],
            'about_video': AboutVideos.objects.all(),
        }


class ContactInformationUrls(TemplateView):
    template_name = 'contact.html'


class TableTimeUrls(ListView):
    model = TableTime
    template_name = 'table-time.html'
    context_object_name = 'tableobject'

    def get_queryset(self):
        return {
            'table': TableTime.objects.all(),
        }


class LessonTableUrls(ListView):
    model = LessonTable
    template_name = 'lesson_table.html'
    context_object_name = 'lessonobject'

    def get_queryset(self):
        return {
            'lesson': LessonTable.objects.order_by('-id'),
        }


class LogoUrls(ListView):
    model = LogoFoto
    template_name = 'base.html'
    context_object_name = 'logoobject'

    def get_queryset(self):
        return LogoFoto.objects.order_by('-id')[:1]


class ContactUrls(ListView):
    model = Contact
    template_name = 'base.html'
    context_object_name = 'contactobject'

    def get_queryset(self):
        return Contact.objects.order_by('-id')[:1]

