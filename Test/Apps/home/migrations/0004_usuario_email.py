# Generated by Django 3.2.7 on 2021-09-28 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='email',
            field=models.EmailField(default='sucorreo@gmial.com', max_length=50),
        ),
    ]
