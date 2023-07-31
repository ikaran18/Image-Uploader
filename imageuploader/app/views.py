from django.shortcuts import render
from .models import *
from .forms import ImageForm

# Create your views here.

def home(request):
    if request.method =="POST":
        fm = ImageForm(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()

    img = Image.objects.all()
    return render(request,'index.html',{'fm':fm,'img':img})