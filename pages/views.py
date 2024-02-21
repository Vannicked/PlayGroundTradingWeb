from django.shortcuts import render

def home(request):
    return render(request, "pages/home.html", {})

def game(request):
    return render(request, "pages/game.html", {})

def education(request):
    return render(request, "pages/education.html", {})

def about(request):
    return render(request, "pages/about.html", {})