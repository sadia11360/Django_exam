from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserForm

def home(request):
    return HttpResponse("Welcome to Django!")
def product(request, id):
    return HttpResponse(f"Product ID: {id}") #returning a response with the product ID

def home_view(request):
    context = {"title": "Home Page", "message": "Hello, Django!"} #creating a dictionary
    return render(request, 'index.html', context)

def languages_view(request):
    languages = ["Python", "Django", "JavaScript"] #creating a list of languages
    return render(request, 'index.html', {'languages': languages})

def user_form_view(request):
    form = UserForm() #creating an instance of the UserForm class
    return render(request, 'form.html', {'form': form})
