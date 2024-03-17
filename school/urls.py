from django.urls import path
from .views import (
    IndexUrls,
    BlogUrls,
    AboutUsUrls,
    ContactInformationUrls,
    TableTimeUrls,
    LessonTableUrls,
    )

urlpatterns = [
    path('', IndexUrls.as_view(), name='index'),
    path('blog/', BlogUrls.as_view(), name='blog'),
    path('about/', AboutUsUrls.as_view(), name='about'),
    path('contact/', ContactInformationUrls.as_view(), name='contact'),
    path('tabletime/', TableTimeUrls.as_view(), name='tabletime'),
    path('lesson-table/', LessonTableUrls.as_view(), name='lesson-table'),
]
