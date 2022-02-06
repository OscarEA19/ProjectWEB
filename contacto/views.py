import email
from .form import Formulario_contacto
from django.shortcuts import redirect, render,HttpResponse
from django.core.mail import send_mail
# Create your views here.



# Create your views here.

def contacto(request):
    formulario_con=Formulario_contacto()
    if request.method=='POST':
        formulario_con=Formulario_contacto(data=request.POST)
        if formulario_con.is_valid():
            nombre=request.POST.get("nombre")
            correo=request.POST.get("email")
            contenido=request.POST.get("contenido")

            
            try:
                send_mail(f'Mensaje parte de: {nombre}',contenido,correo,['keosaleedu@gmail.com'],fail_silently=False,) 
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?noValido")
            



    return render(request,'contacto/contacto.html',{"myformulario":formulario_con})

