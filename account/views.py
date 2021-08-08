from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from .models import User
from .forms import RegistrationForm, UpdateForm


# Представление регистрации user'а
class RegisterView(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'account/registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy("home")
    success_message = 'Новый user создан!'


# Представление входа user'а
class SignInView(LoginView):
    template_name = 'account/login.html'


# Представление профиля user'а
def profile(request):
    return render(request, 'account/profile.html')



# class UpdateUserView(SuccessMessageMixin, UpdateView):
#     pk_url_kwarg = 'pk'
#     model = User
#     template_name = 'account/update-profile.html'
#     form_class = RegistrationForm
#     success_url = reverse_lazy("home")
#     success_message = 'Успешно данные изменены!'


class UpdateUserView(UpdateView):
    pk_url_kwarg = 'id'
    model = User
    template_name = 'account/update-profile.html'
    form_class = UpdateForm
    success_url = reverse_lazy("home")
    success_message = 'Данные изменены!'
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['user_form'] = self.get_form(self.get_form_class())
    #     return context



