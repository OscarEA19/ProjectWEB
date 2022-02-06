
from django import forms

class Formulario_contacto(forms.Form):
    nombre=forms.CharField(label="Nombre",required=True, max_length=30)
    email=forms.EmailField(label="Correo Electronico",required=True ,max_length=50)
    contenido=forms.CharField(label="Mensaje",required=True,max_length=100,widget=forms.Textarea)