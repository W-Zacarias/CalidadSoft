from django.db import models

# Create your models here.
class Departamento(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return '%s' % (self.nombre)



class Usuario(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    
    email=models.EmailField(max_length = 254)
    contraseña=models.CharField(max_length=50)
    creacion=models.DateField(auto_now_add=True)
    actualizacion=models.DateField(auto_now_add=True)


    def __str__(self):
        return '%s %s %s %s' % (self.nombre, self.apellido, self.email, self.contraseña)

class FormularioInscripcion(models.Model):
    IDusuario=models.ForeignKey(
        'Usuario',
        on_delete=models.CASCADE,
        default=1
    )
    gene =(
        ('M', 'Masculino'),
        ('F','Femenino'),
        ('X','Otro')
    )
    edad=models.CharField(max_length=10)
    sexo=models.CharField(max_length=20, choices=gene)
    IDDepartamentos=models.ForeignKey(
        'Departamento',
        on_delete=models.CASCADE,
        default=1
        )
    dMunicipioDireccionDeRecibido=models.CharField(max_length=250)
    fotografiaPersonal=models.FileField(upload_to = "Uploaded Files/")
    cartaRecomendacion=models.FileField(upload_to = "Uploaded Files/")
    cartaLaboral=models.FileField(upload_to = "Uploaded Files/")
    tituloyDiplomas=models.FileField(upload_to = "Uploaded Files/")
    CUI=models.CharField(max_length=15)
    fotografiaDPI=models.FileField(upload_to = "Uploaded Files/")
    fotografiaRTU=models.FileField(upload_to = "Uploaded Files/")
    antecedentespenales=models.FileField(upload_to = "Uploaded Files/")
    antecedentespoliciacos=models.FileField(upload_to = "Uploaded Files/")
    creacion=models.DateField(auto_now_add=True)
    actualizacion=models.DateField(auto_now_add=True)


    def __str__(self):
        return '%s %s %s %s %s %s %s %s %s %s %s %s' % (self.edad, self.sexo, self.dMunicipioDireccionDeRecibido, self.fotografiaPersonal, self.cartaRecomendacion, self.cartaLaboral, self.tituloyDiplomas, self.CUI, self.fotografiaDPI, self.fotografiaRTU, self.antecedentespenales, self.antecedentespoliciacos)

class Profesion(models.Model):
    profesion=models.CharField(max_length=50)
   
    def __str__(self):
        return '%s ' % (self.profesion)

class Formulario_Profesion(models.Model):
    IDFormulario=models.ForeignKey(
        'FormularioInscripcion',
        on_delete=models.CASCADE,
        default=1
        )
    IDProfesion=models.ForeignKey(
        'Profesion',
        on_delete=models.CASCADE,
        default=1
        )
 
    def __str__(self):
        return '' % ()

class UsuarioAdmin(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    contraseña=models.CharField(max_length=50)
    puesto=models.CharField(max_length=50)
    creacion=models.DateField(auto_now_add=True)
    actualizacion=models.DateField(auto_now_add=True)


    def __str__(self):
        return '%s %s %s %s' % (self.nombre, self.apellido, self.contraseña, self.puesto)

class Reuniones(models.Model):
    motivo=models.CharField(max_length=500)
    tipo=models.CharField(max_length=50)
    horaRegisto=models.DateTimeField()
    horaReunion=models.DateTimeField()
    IDUsuarioAdmin=models.ForeignKey(
        'UsuarioAdmin',
        on_delete=models.CASCADE,
        default=1
        )
    creacion=models.DateField(auto_now_add=True)
    actualizacion=models.DateField(auto_now_add=True)


    def __str__(self):
        return '%s %s %s %s' % (self.motivo, self.tipo, self.horaRegisto, self.horaReunion)

class Asistencia(models.Model):
    IDFormulario=models.ForeignKey(
        'FormularioInscripcion',
        on_delete=models.CASCADE,
        default=1
        )
    IDReuniones=models.ForeignKey(
        'Reuniones',
        on_delete=models.CASCADE,
        default=1
        )
 
    def __str__(self):
        return '' % ()

class Formulario_Reuniones(models.Model):
    IDFormulario=models.ForeignKey(
        'FormularioInscripcion',
        on_delete=models.CASCADE,
        default=1
        )
    IDReuniones=models.ForeignKey(
        'Reuniones',
        on_delete=models.CASCADE,
        default=1
        )
 
    def __str__(self):
        return '' % ()