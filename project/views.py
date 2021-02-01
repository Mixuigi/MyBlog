from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserForm
from .models import Person


def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        country = request.POST.get("country")
        password = request.POST.get("password")

        return HttpResponse(f'<h1> Hello, {name} he  {age} years, Your country is {country}</h2> ')
    else:
        userform = UserForm()
        return render(request, 'index.html', {'form': userform})


def BD(request):
    if request.method == 'POST':
        tom = Person()
        tom.name = request.POST.get('name')
        tom.age = request.POST.get('age')
        tom.save()
        return HttpResponseRedirect('/')
    else:
        people = Person.objects.all()
        return render(request, 'home.html', {'people': people})
