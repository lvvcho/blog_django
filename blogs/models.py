from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.
#categorias,comentarios.etc


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)  #definimos que el post tenga un slug unico ej:http://127.0.0.1:8000/viaje-a-nose
    overview = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True) #de manerea automatica le pone el objeto datetimefield a date_created en el momento q se crea un post
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT) #q modelo se relaciona el post,  si la instancia la borramos lo q se hace es protect (no estamos permitiendo q se borre ese usuario q tiene el post)
    categories = models.ManyToManyField('Category') #MANYTOMANYFIELDS: un post puede tener varias categorias Y UNA CATEGORIA VARIOS POSTS
    featured = models.BooleanField(default=False)  #post destacados

    #funcion q da en el buscador url que ponga el slug al final del url
   
    
    
    def __str__(self): 
        return self.title


class Category(models.Model): #definir le modelo de categorias
    #tiene 2 atributos titulo y slug
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = 'categories' #por error de django cambiamos el pural de category a categories



    def __str__(self):
        return self.title