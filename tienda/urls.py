from tienda import views
from django.urls import path


urlpatterns = [
    path('',views.tienda,name="Tienda"),
]

