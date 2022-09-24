from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy

from .forms import FormAdmin, FormIncripcion, FormUser
from .models import FormularioInscripcion, Usuario, UsuarioAdmin

# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'

class InicioView(TemplateView):
    template_name = 'home.html'

class StoreView(TemplateView):
    template_name = 'store.html'

class Home2View(TemplateView):
    template_name = 'index2.html'

class DocsView(TemplateView):
    template_name = 'documentos.html'

class FormsoView(CreateView):
    model = FormularioInscripcion
    form_class = FormIncripcion
    template_name = 'formularios.html'
    success_url = reverse_lazy('home')

class MeetView(TemplateView):
    template_name = 'reuniones.html'

class LoginView(TemplateView):
    template_name = 'LogIn.html'

class RegistroView(TemplateView):
    template_name = 'registrar.html'

class RegistroAdminView(CreateView):
    model = UsuarioAdmin
    form_class = FormAdmin
    template_name = 'registrarAdmin.html'
    success_url = reverse_lazy('home')

class RegistroUserView(CreateView):
    model = Usuario
    form_class = FormUser
    template_name = 'registrarUsuario.html'
    success_url = reverse_lazy('home')