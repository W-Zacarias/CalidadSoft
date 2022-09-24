from django.contrib import admin
from django.urls import path
from .views import HomeView,InicioView,DocsView,FormsoView, LoginView,MeetView, RegistroAdminView, RegistroUserView, RegistroView, Home2View, StoreView

 

urlpatterns = [
    path('index/', HomeView.as_view(), name='index'),
    path('home/', InicioView.as_view(), name='home'),
    path('documentos/', DocsView.as_view(), name='documentos'),
    path('reuniones/', MeetView.as_view(), name='reuniones'),
    path('formularios/', FormsoView.as_view(), name='formularios'),
    path('login/', LoginView.as_view(), name='login'),
    path('index2/', Home2View.as_view(), name='index2'),
    path('store/', StoreView.as_view(), name='store'),

    
    path('registrar/', RegistroView.as_view(), name='registrar'),
    path('registrarAdmin/', RegistroAdminView.as_view(), name='registrarAdmin'),
    path('registrarUser/', RegistroUserView.as_view(), name='registrarUser'),
]