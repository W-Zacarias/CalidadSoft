# Generated by Django 3.2.7 on 2021-10-01 01:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_usuarioadmin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reuniones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo', models.CharField(max_length=500)),
                ('tipo', models.CharField(max_length=50)),
                ('horaRegisto', models.DateTimeField()),
                ('horaReunion', models.DateTimeField()),
                ('creacion', models.DateField(auto_now_add=True)),
                ('actualizacion', models.DateField(auto_now_add=True)),
                ('IDUsuarioAdmin', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.usuarioadmin')),
            ],
        ),
    ]
