from django import forms

from .models import FormularioInscripcion, Usuario, UsuarioAdmin


class FormIncripcion(forms.ModelForm):
    class Meta:
        model = FormularioInscripcion
        fields=[
            'IDusuario',
            'edad',
            'sexo',
            'IDDepartamentos',
            'dMunicipioDireccionDeRecibido',
            'fotografiaPersonal',
            'cartaRecomendacion',
            'cartaLaboral',
            'tituloyDiplomas',
            'CUI',
            'fotografiaDPI',
            'fotografiaRTU',
            'antecedentespenales',
            'antecedentespoliciacos',
            

        ]
        labels ={
            'IDusuario':'Usuario',
            'edad':'Edad',
            'sexo':'Sexo',
            'IDDepartamentos':'Departamento',
            'dMunicipioDireccionDeRecibido':'Direccion',
            'fotografiaPersonal':'Fotografia Personal',
            'cartaRecomendacion':'Cartas de Recomendacion',
            'cartaLaboral':'Cartas Laborales',
            'tituloyDiplomas':'Titulos y/o Diplomas',
            'CUI':'CUI',
            'fotografiaDPI':'Fotografia de DPI',
            'fotografiaRTU':'Fotografia de RTU',
            'antecedentespenales':'Antecedentes Penales',
            'antecedentespoliciacos':'Antecedentes Policiacos',
            
        }

class FormUser(forms.ModelForm):
    class Meta:
        model = Usuario 
        fields=[
            'nombre',
            'apellido',
            'email',
            'contraseña',
            

        ]
        labels ={
            'nombre':'Nombres',
            'apellido':'Apellidos',
            'email':'Correo Electronico',
            'contraseña':'Contraseña',
            
            
        }

class FormAdmin(forms.ModelForm):
    class Meta:
        model =UsuarioAdmin  
        fields=[
            'nombre',
            'apellido',
            'contraseña',
            'puesto',
            

        ]
        labels ={
            
            'nombre':'Nombres',
            'apellido':'Apellidos',
            'contraseña':'Contraseña',
            'puesto':'Puesto',
        }