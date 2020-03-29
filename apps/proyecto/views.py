from datetime import date, timedelta
from io import BytesIO

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User



def index(request):
    return render(request, 'proyecto/index.html')


class UsuarioList(LoginRequiredMixin, ListView):
    model = User
    template_name = 'proyecto/lista_usuarios.html'
    context_object_name = 'user_list'
    paginate_by = 10