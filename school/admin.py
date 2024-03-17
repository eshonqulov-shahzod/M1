from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import (
    HomePhoto1,
    HomeBlog,
    HomePhotoRoom,
    HomePhotoUniform,
    AboutVideos,
    AboutGallery,
    AboutName,
    AboutStaff,
    TableTime,
    LessonTable,
    LogoFoto,
    Contact,
    )

# Register your models here.


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('name', 'foto')

    def foto(self, obj):
        return mark_safe(f'<img src="{obj.photo.url}" width="100" height="100" />')


class GalleryAdminUniform(admin.ModelAdmin):
    list_display = ('detail', 'foto')

    def foto(self, obj):
        return mark_safe(f'<img src="{obj.photo.url}" width="100" height="100" />')


admin.site.register(Contact)
admin.site.register(LogoFoto, GalleryAdmin)
admin.site.register(HomePhoto1, GalleryAdmin)
admin.site.register(HomeBlog, GalleryAdmin)
admin.site.register(HomePhotoRoom, GalleryAdmin)
admin.site.register(HomePhotoUniform, GalleryAdminUniform)
admin.site.register(AboutVideos, GalleryAdmin)
admin.site.register(AboutGallery, GalleryAdmin)
admin.site.register(AboutName)
admin.site.register(AboutStaff, GalleryAdmin)
admin.site.register(TableTime, GalleryAdmin)
admin.site.register(LessonTable, GalleryAdmin)


