from django.urls import path
from .views import (
    IndexUrls,
    HomeBlogListView,
    HomeBlogDetailView,
    AboutUsUrls,
    ContactInformationUrls,
    TableTimeUrls,
    LessonTableUrls,
    )

urlpatterns = [
    path('', IndexUrls.as_view(), name='index'),
    path('blog/', HomeBlogListView.as_view(), name='blog'),
    path('blog/<int:pk>/', HomeBlogDetailView.as_view(), name='homeblog_detail'),
    path('about/', AboutUsUrls.as_view(), name='about'),
    path('contact/', ContactInformationUrls.as_view(), name='contact'),
    path('tabletime/', TableTimeUrls.as_view(), name='tabletime'),
    path('lesson-table/', LessonTableUrls.as_view(), name='lesson-table'),
]
