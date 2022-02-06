from xml.dom.minidom import Document
from . import views
from django.urls import path

from django.conf.urls.static import static

urlpatterns = [
    path('',views.servicios,name="Servicios"),
]

