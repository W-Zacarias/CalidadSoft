# Generated by Django 3.2.7 on 2021-10-01 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_formulario_profesion'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsuarioAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('contraseña', models.CharField(max_length=50)),
                ('puesto', models.CharField(max_length=50)),
                ('creacion', models.DateField(auto_now_add=True)),
                ('actualizacion', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
