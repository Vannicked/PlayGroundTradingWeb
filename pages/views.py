from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import buyForm, sellForm
from .models import Portfolio

def home(request):
    return render(request, "pages/home.html", {})

def game(request):
    if request.method == "POST":
        buying = buyForm(request.POST)
        selling = sellForm(request.POST)
        
        if buying.is_valid():
            p = Portfolio.objects.all()[0]
            boughtStock = buying.cleaned_data['stock'].lower()
            sharesBought = buying.cleaned_data['shares']
            checkStock(p, boughtStock, sharesBought)
            p.save()
            print("You have bought a stock!")
        if selling.is_valid():
            p = Portfolio.objects.all()[0]
            soldStock = selling.cleaned_data['stock'].lower()
            sharesSold = -abs(selling.cleaned_data['shares'])
            checkStock(p, soldStock, sharesSold)
            p.save()
            print("You have sold a stock!")
        
    else:
        x = Portfolio.objects.count() 
        if x < 1:
            p = Portfolio(aal=0, aapl=0, amzn=0, bac=0, dal=0, hmc=0, jnj=0, jpm=0, lly=0, luv=0, msft=0, tm=0, tsla=0, unh=0, v=0)
            p.save()
        buying = buyForm()
        selling = sellForm()

    return render(request, "pages/game.html", {"buying": buyForm, "selling": sellForm})

def education(request):
    return render(request, "pages/education.html", {})

def about(request):
    return render(request, "pages/about.html", {})

def checkStock(p, stock_name, num_shares):
    if (stock_name == 'aal'):
        p.aal = p.aal + num_shares
    elif (stock_name == 'aapl'):
        p.aapl = p.aapl + num_shares
    elif (stock_name == 'amzn'):
        p.amzn = p.amzn + num_shares
    elif (stock_name == 'bac'):
        p.bac = p.bac + num_shares
    elif (stock_name == 'dal'):
        p.dal = p.dal + num_shares
    elif (stock_name == 'hmc'):
        p.hmc = p.hmc + num_shares
    elif (stock_name == 'jnj'):
        p.jnj = p.jnj + num_shares
    elif (stock_name == 'jpm'):
        p.jpm = p.jpm + num_shares
    elif (stock_name == 'lly'):
        p.lly = p.lly + num_shares
    elif (stock_name == 'luv'):
        p.luv = p.luv + num_shares
    elif (stock_name == 'msft'):
        p.msft = p.msft + num_shares
    elif (stock_name == 'tm'):
        p.tm = p.tm + num_shares
    elif (stock_name == 'tsla'):
        p.tsla = p.tsla + num_shares
    elif (stock_name == 'unh'):
        p.unh = p.unh + num_shares
    else:
        p.v = p.v + num_shares