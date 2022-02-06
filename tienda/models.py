from distutils.archive_util import make_zipfile
from distutils.command.upload import upload
from mailbox import NoSuchMailboxError
from pyexpat import model
from re import VERBOSE
from tabnanny import verbose
from tkinter import image_names
from django.db import models

# Create your models here.


class CategoriasProd(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now_add=True)
    class Meta():
        verbose_name="categoriasProd"
        verbose_name_plural="categoriasProd"
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    categorias=models.ForeignKey(CategoriasProd, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to="tienda",null=True,blank=True)
    precio=models.FloatField()
    disponibilidad=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name="Producto"
        verbose_name_plural="Productos"

    def  __str__(self):
        return f'{self.nombre} , Precio: {self.precio}'
