from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Workers, Teachers, Students


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


class StudentsListView1(LoginRequiredMixin, ListView):
    model = Students
    template_name = 'students_list_1.html'


class StudentsListView2(LoginRequiredMixin, ListView):
    model = Students
    template_name = 'students_list_2.html'


class StudentsListView3(LoginRequiredMixin, ListView):
    model = Students
    template_name = 'students_list_3.html'


class StudentsListView4(LoginRequiredMixin, ListView):
    model = Students
    template_name = 'students_list_4.html'


class StudentsListView5(LoginRequiredMixin, ListView):
    model = Students
    template_name = 'students_list_5.html'


class StudentsListView6(LoginRequiredMixin, ListView):
    model = Students
    template_name = 'students_list_6.html'


class StudentsListView7(LoginRequiredMixin, ListView):
    model = Students
    template_name = 'students_list_7.html'


class StudentsListView8(LoginRequiredMixin, ListView):
    model = Students
    template_name = 'students_list_8.html'


class StudentsListView9(LoginRequiredMixin, ListView):
    model = Students
    template_name = 'students_list_9.html'


class StudentsListView10(LoginRequiredMixin, ListView):
    model = Students
    template_name = 'students_list_10.html'


class StudentsListView11(LoginRequiredMixin, ListView):
    model = Students
    template_name = 'students_list_11.html'


class StudentsDetailView(LoginRequiredMixin, DetailView):
    model = Students
    template_name = 'students_detail.html'


class StudentsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Students
    fields = ('name', 'class_id', 'class_letter', 'name_father', 'name_mom', 'phone_father', 'phone_mom', 'photo')
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
    fields = ('name', 'class_id', 'class_letter', 'name_father', 'name_mom', 'phone_father', 'phone_mom', 'photo')
    template_name = 'students_new.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser





