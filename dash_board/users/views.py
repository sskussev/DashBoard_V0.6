from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import UserPassesTestMixin

from .forms import CustomUserCreationForm


# class SignUp(CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('board:index')
#     template_name = 'users/signup.html'

class SignUp(UserPassesTestMixin, CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('board:index')
    template_name = 'users/signup.html'

    def test_func(self):
        return self.request.user.is_staff