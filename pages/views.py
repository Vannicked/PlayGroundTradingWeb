from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import buyForm, sellForm

def home(request):
    return render(request, "pages/home.html", {})

def game(request):
    if request.method == "POST":
        buying = buyForm(request.POST)
        selling = sellForm(request.POST)
        
        if buying.is_valid():
            print("You have bought a stock!")
        if selling.is_valid():
            print("You have sold a stock!")
        
    else:
        buying = buyForm()
        selling = sellForm()

    return render(request, "pages/game.html", {"buying": buyForm, "selling": sellForm})

def education(request):
    return render(request, "pages/education.html", {})

def about(request):
    return render(request, "pages/about.html", {})

def quiz(request):
    return render(request, "pages/quiz.html", {})