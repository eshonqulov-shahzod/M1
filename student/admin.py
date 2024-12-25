from django.contrib import admin
from .models import Workers, Teachers, ClassName, Students, News

# Register your models here.

admin.site.register(Workers)
admin.site.register(Teachers)
admin.site.register(ClassName)
admin.site.register(Students)
admin.site.register(News)

