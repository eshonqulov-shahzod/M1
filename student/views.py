from django.views.generic import ListView, TemplateView, DetailView
from django.http import HttpResponseForbidden
from django.template.loader import render_to_string
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Workers, Teachers, Students, ClassName, News


def my_custom_403_view(request, exception=None):
    # Maxsus 403 xatolik sahifasini ko'rsatish
    html = render_to_string('403.html', {'request': request})
    return HttpResponseForbidden(html)


# Yangiliklar ro'yxati uchun CBV
class NewsListView(LoginRequiredMixin, ListView):
    model = News
    template_name = 'home.html'  # Yangiliklar ro'yxati shabloni
    context_object_name = 'news_list'  # Shablonga o'tadigan kontekst nomi
    ordering = ['-created_at']  # Yaratilgan vaqt bo'yicha teskari tartib


# Yangilik tafsilotlari uchun CBV
class NewsDetailView(LoginRequiredMixin, DetailView):
    model = News
    template_name = 'home_new.html'  # Yangilik tafsiloti shabloni
    context_object_name = 'news'  # Shablonga o'tadigan kontekst nomi


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'


class WorkersListView(LoginRequiredMixin, ListView):
    model = Workers
    template_name = 'workers_list.html'


class WorkersDetailView(LoginRequiredMixin, DetailView):
    model = Workers
    template_name = 'workers_detail.html'


class WorkersUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Workers
    fields = ('name', 'position', 'phone', 'photo',)
    template_name = 'workers_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class WorkersDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Workers
    template_name = 'workers_delete.html'
    success_url = reverse_lazy('workers_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class WorkersCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Workers
    fields = ('name', 'position', 'phone', 'photo')
    template_name = 'workers_new.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser


class TeachersListView(LoginRequiredMixin, ListView):
    model = Teachers
    template_name = 'teachers_list.html'


class TeachersDetailView(LoginRequiredMixin, DetailView):
    model = Teachers
    template_name = 'teachers_detail.html'


class TeachersUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Teachers
    fields = ('name', 'position', 'phone', 'working_time', 'photo', 'level')
    template_name = 'teachers_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class TeachersDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Teachers
    template_name = 'teachers_delete.html'
    success_url = reverse_lazy('teachers_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class TeachersCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Teachers
    fields = ('name', 'position', 'phone', 'working_time', 'photo', 'level')
    template_name = 'teachers_new.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser


#def class_students(request, class_id, class_letter):
#    students = Students.objects.filter(class_id=class_id, class_letter__iexact=class_letter)
#    context = {
#        'students': students,
#        'class_id': class_id,
#        'class_letter': class_letter.upper(),
#    }
#    return render(request, 'class_students.html', context)


class ClassNameView(LoginRequiredMixin, ListView):
    model = ClassName
    template_name = 'class_list.html'


#class ClassNameView(LoginRequiredMixin, ListView):
#    template_name = 'base2.html'
#
#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context['names'] = ClassName.objects.all()  # Ma'lumotlar bazasidan obyektlar
#        print(context['menu_items'])
#        return context


class StudentsListView(LoginRequiredMixin, ListView):
    model = Students
    template_name = 'students_list.html'
    context_object_name = 'students_list'

    def get_queryset(self):
        # URL orqali kelgan sinf `pk` bo‘yicha talabalarni filtrlash
        return Students.objects.filter(class_name_id=self.kwargs['pk'])


#class StudentsListView2(LoginRequiredMixin, ListView):
#    model = Students
#    template_name = 'students_list_2.html'
#
#
#class StudentsListView3(LoginRequiredMixin, ListView):
#    model = Students
#    template_name = 'students_list_3.html'
#
#
#class StudentsListView4(LoginRequiredMixin, ListView):
#    model = Students
#    template_name = 'students_list_4.html'
#
#
#class StudentsListView5(LoginRequiredMixin, ListView):
#    model = Students
#    template_name = 'students_list_5.html'
#
#
#class StudentsListView6(LoginRequiredMixin, ListView):
#    model = Students
#    template_name = 'students_list_6.html'
#
#
#class StudentsListView7(LoginRequiredMixin, ListView):
#    model = Students
#    template_name = 'students_list_7.html'
#
#
#class StudentsListView8(LoginRequiredMixin, ListView):
#    model = Students
#    template_name = 'students_list_8.html'
#
#
#class StudentsListView9(LoginRequiredMixin, ListView):
#    model = Students
#    template_name = 'students_list_9.html'
#
#
#class StudentsListView10(LoginRequiredMixin, ListView):
#    model = Students
#    template_name = 'students_list_10.html'
#
#
#class StudentsListView11(LoginRequiredMixin, ListView):
#    model = Students
#    template_name = 'students_list_11.html'


class StudentsDetailView(LoginRequiredMixin, DetailView):
    model = Students
    template_name = 'students_detail.html'


class StudentsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Students
    fields = ('name', 'class_name', 'name_father', 'name_mom',
              'phone_father', 'phone_mom', 'photo')
    template_name = 'students_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class StudentsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Students
    template_name = 'students_delete.html'
    success_url = reverse_lazy('students_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class StudentsCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Students
    fields = ('name', 'class_id', 'class_letter', 'name_father', 'name_mom',
              'phone_father', 'phone_mom', 'photo', 'class_head')
    template_name = 'students_new.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser





