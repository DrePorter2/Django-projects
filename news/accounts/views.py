from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomAccountCreationForm


class SignUpView(CreateView):
    form_class = CustomAccountCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
