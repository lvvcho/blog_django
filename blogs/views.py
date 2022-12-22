from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from blogs.models import Post, Category

# Create your views here.

def home_page(request):
   posts = Post.objects.all() #con esto conseguimos todos los post q tenemos
   categories = Category.objects.all()
   featured = Post.objects.filter(featured=True) [:3] #queremos que se pasen los primeros 3 post destacados

   context = {
        'posts': posts,
        'categories': categories,
        'featured': featured
   }

   return render(request, 'blogs/home_page.html', context=context) #le pasamos el equest, el temple q utilizaremos y el contexto
   


class PostDetailView(generic.DetailView):
     model = Post
     
     
     
     
    