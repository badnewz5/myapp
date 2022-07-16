from django.shortcuts import render,redirect
from user.models import*


# Create your views here.

def home(request):
    blogs = Blog.objects.all()
    profiles = Details.objects.all()
    context={'blogs':blogs,'profiles':profiles}
    return render(request , 'Pages/index.html',context)
