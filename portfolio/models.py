from distutils.command.upload import upload
from email.mime import image
from os import link
from pickle import TRUE
from turtle import title
from django.db import models

# Create your models here.

class Project(models.Model): #esta clase represencta una tabla dentro de la base de datos
    title = models.CharField(max_length=200, verbose_name= "titulo")
    description = models.TextField(verbose_name= "descripcion")
    image = models.ImageField(verbose_name= "imagen", upload_to = "projects")
    link= models.URLField(verbose_name= "Direccion Web",null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True,verbose_name= "fecha de cracion") #se añade la hora automaticamente cuando se crea la primera vez
    updated = models.DateTimeField(auto_now=True,verbose_name= "fecha de edicion") #se ejecuta cada vez que hay una instancia

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"]

    def __str__(self): #metodo string 
        return self.title #retorna el titulo del proyecto

