from django.contrib import admin
from .models import Asistencia, Departamento, Formulario_Reuniones, FormularioInscripcion,  Profesion, Reuniones, Usuario, Formulario_Profesion, UsuarioAdmin
# Register your models here.
admin.site.register(Departamento)

admin.site.register(Usuario)
admin.site.register(FormularioInscripcion)
admin.site.register(Profesion)
admin.site.register(Formulario_Profesion)
admin.site.register(UsuarioAdmin)
admin.site.register(Reuniones)
admin.site.register(Asistencia)
admin.site.register(Formulario_Reuniones)