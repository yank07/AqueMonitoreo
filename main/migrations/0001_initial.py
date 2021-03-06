# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-11 21:33
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=500)),
                ('contenido', tinymce.models.HTMLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Distrito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Complete con un nombre de Distrito/ciudad/Pais/Governacion. Ej: Luque', max_length=200)),
                ('descripcion', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Eje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Complete con un nombre de Eje. Ej: Educacion', max_length=200)),
                ('breve_explicacion', models.CharField(blank=True, max_length=200)),
                ('imagen', models.ImageField(upload_to=b'', verbose_name='Image')),
                ('distrito', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ejes', to='main.Distrito')),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta', models.CharField(help_text='Escriba la pregunta o compromiso hecho al mandatario', max_length=500)),
                ('estado', models.CharField(choices=[('Sin Esdado', 'Sin Estado'), ('Aprobado', 'Aprobado'), ('No aprobado', 'No aprobado')], default='Sin Estado', max_length=15)),
                ('respuesta', ckeditor.fields.RichTextField(blank=True, default='')),
                ('eje', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='preguntas', to='main.Eje')),
            ],
        ),
        migrations.AddField(
            model_name='articulo',
            name='pregunta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articulos', to='main.Pregunta'),
        ),
    ]
