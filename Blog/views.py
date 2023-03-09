from django.shortcuts import render
from Blog.models import Post, Categorias

# Create your views here.

def blog(request):
    posts= Post.objects.all()

    return render(request, "Blog/blog.html", {"posts":posts})

def categoria(request, categorias_id):
    categoria= Categorias.objects.get(id=categorias_id)
    posts= Post.objects.filter(cates=categoria)

    return render(request, "Blog/filtrado.html", {"posts": posts, "categoria":categoria})