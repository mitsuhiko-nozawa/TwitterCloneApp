from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from . import forms

class SignUpView(generic.CreateView):
    form_class = forms.SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
