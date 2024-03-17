#from django.views.generic import ListView
#from django.views.generic.edit import UpdateView
#from django.shortcuts import render
#from .models import (
#    HomePhoto1,
#    HomeBlog,
#    HomePhotoUniform,
#    HomePhotoRoom,
#    AboutName,
#    AboutStaff,
#    AboutGallery,
#    AboutVideos,
#    ContactMap,
#    ContactAddress
#    )
#
## Create your views here.
#
#
#class HomeView(ListView):
#    model = HomePhoto1
#    template_name = 'index.html'
#    context_object_name = 'homeobject'
#
#    def get_queryset(self):
#        return {
#            'home-photo1': HomePhoto1.objects.all(),
#            'home-blog': HomeBlog.objects.all(),
#            'home-uniform': HomePhotoUniform.objects.all(),
#            'home-room': HomePhotoRoom.objects.all(),
#        }
#
#
#class HomeBlogUpdateView(ListView):
#    model = HomeBlog
#    #fields = ('name', 'short_name', 'photo', 'detail', 'data')
#    template_name = 'blog.html'
#
#
#class AboutView(ListView):
#    model = AboutName
#    template_name = 'about.html'
#    context_object_name = 'aboutobject'
#
#    def get_queryset(self):
#        return {
#            'about-name': AboutName.objects.all(),
#            'about-staff': AboutStaff.objects.all(),
#            'about-gallery': AboutGallery.objects.all(),
#            'about-video': AboutVideos.objects.all(),
#        }


#class HomePhoto1UpdateView(ListView):
#    model = HomePhoto1
#    #fields = ('name', 'address', 'photo')
#    template_name = 'index.html'
#
#
#class HomePhotoUniformUpdateView(ListView):
#    model = HomePhotoUniform
#    #fields = ('detail', 'photo')
#    template_name = 'index.html'
#
#
#class HomePhotoRoomUpdateView(ListView):
#    model = HomePhotoRoom
#    #fields = ('name', 'detail', 'photo')
#    template_name = 'index.html'
#


#class AboutNameUpdateView(ListView):
#    model = AboutName
#    #fields = ('name', 'detail')
#    template_name = 'about.html'
#
#
#class AboutStaffUpdateView(ListView):
#    model = AboutStaff
#    #fields = ('name', 'photo', 'staff', 'level')
#    template_name = 'about.html'
#
#
#class AboutGalleryUpdateView(ListView):
#    model = AboutGallery
#    #fields = ('name', 'photo')
#    template_name = 'about.html'
#
#
#class AboutVideosUpdateView(ListView):
#    model = AboutVideos
#    #fields = ('name', 'video')
#    template_name = 'about.html'
#
