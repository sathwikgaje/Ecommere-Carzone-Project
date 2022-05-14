from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def view(request):
    return render(request,'pages/hello.html')

def about(request):
    return render(request,'pages/about.html')

def services(request):
    return render(request,'pages/services.html')

def contact(request):
    return render(request,'pages/contact.html')
