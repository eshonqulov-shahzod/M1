from django.urls import path
from . import views
from django.conf.urls import handler403
from .views import (
    my_custom_403_view,
    NewsListView,
    NewsDetailView,
    WorkersListView,
    WorkersUpdateView,
    WorkersDeleteView,
    WorkersDetailView,
    WorkersCreateView,
    TeachersListView,
    TeachersUpdateView,
    TeachersDeleteView,
    TeachersDetailView,
    TeachersCreateView,
    StudentsListView,
    ClassNameView,
    StudentsUpdateView,
    StudentsDeleteView,
    StudentsDetailView,
    StudentsCreateView,
    HomeView)


# 403 xatolikni sozlash
handler403 = my_custom_403_view


urlpatterns = [
    path('', NewsListView.as_view(), name='news_list'),  # Yangiliklar ro'yxati
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),  # Yangilik tafsiloti
    path('workers/', WorkersListView.as_view(), name='workers_list'),
    path('<int:pk>/edit-w/', WorkersUpdateView.as_view(), name='workers_edit'),
    path('<int:pk>/delete-w/', WorkersDeleteView.as_view(), name='workers_delete'),
    path('<int:pk>/detail-w/', WorkersDetailView.as_view(), name='workers_detail'),
    path('new-w/', WorkersCreateView.as_view(), name='workers_new'),
    path('teachers/', TeachersListView.as_view(), name='teachers_list'),
    path('<int:pk>/edit-t/', TeachersUpdateView.as_view(), name='teachers_edit'),
    path('<int:pk>/delete-t/', TeachersDeleteView.as_view(), name='teachers_delete'),
    path('<int:pk>/detail-t/', TeachersDetailView.as_view(), name='teachers_detail'),
    path('new-t/', TeachersCreateView.as_view(), name='teachers_new'),
    path('list-s/<int:pk>/', StudentsListView.as_view(), name='students_list'),
    path('class-n/', ClassNameView.as_view(), name='class_name'),
    path('<int:pk>/edit-s/', StudentsUpdateView.as_view(), name='students_edit'),
    path('<int:pk>/delete-s/', StudentsDeleteView.as_view(), name='students_delete'),
    path('<int:pk>/detail-s/', StudentsDetailView.as_view(), name='students_detail'),
    path('new-s/', StudentsCreateView.as_view(), name='students_new'),

]
