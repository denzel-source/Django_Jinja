from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def base(request):
    return render(request, 'base.html')
def services(request):
    return render(request, 'services.html')