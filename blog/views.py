
from django.shortcuts import render
from markupsafe import re

from blog.models import Categoria, Post

# Create your views here.

def imprimircategorias(posts):
    cate=[]
    for post in posts:
        for categoria in post.categorias.all():
            cate.append(categoria)
    return set(cate)
    
def blog(request):
    posts=Post.objects.all()
    
    mycategorias=imprimircategorias(posts)

    return render(request,'blog/blog.html',{"posts":posts,"categorias":mycategorias})

def categoria(request,categoria_id):
    categoria=Categoria.objects.get(id=categoria_id)
    posts=Post.objects.filter(categorias=categoria)
    mycategorias=imprimircategorias(posts)
    return render(request,'blog/categoria.html',{"categoria":categoria,"posts":posts,"categorias":mycategorias})