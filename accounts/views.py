from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import UserPassesTestMixin
from .forms import CustomUserCreationForm


class SingUpView(UserPassesTestMixin, CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/singup.html'

    def test_func(self):
        return self.request.user.is_superuser

