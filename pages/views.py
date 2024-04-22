from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import stockActions
from .models import Portfolio

import pandas as pd

def home(request):
    return render(request, "pages/home.html", {})

def game(request):
    if request.method == "POST":
        stockActionsForm = stockActions(request.POST)

        if 'buy_stock' in request.POST:
            if stockActionsForm.is_valid():
                p = Portfolio.objects.all()[0]
                boughtStock = stockActionsForm.cleaned_data['stock'].lower()
                sharesBought = stockActionsForm.cleaned_data['shares']
                checkStock(p, boughtStock, sharesBought)
                p.save()
                print("You have bought a stock!")
        elif 'sell_stock' in request.POST:
            if stockActionsForm.is_valid():
                p = Portfolio.objects.all()[0]
                soldStock = stockActionsForm.cleaned_data['stock'].lower()
                sharesSold = -abs(stockActionsForm.cleaned_data['shares'])
                checkStock(p, soldStock, sharesSold)
                p.save()
                print("You have sold a stock!")
    else:
        x = Portfolio.objects.count() 
        if x < 1:
            p = Portfolio(aal=0, aapl=0, amzn=0, bac=0, dal=0, hmc=0, jnj=0, jpm=0, lly=0, luv=0, msft=0, tm=0, tsla=0, unh=0, v=0)
            p.save()
        stockActionsForm = stockActions()

    stockTable = pd.read_csv('pages/static/pages/StockPrices.csv')
    shownMonths = 6
    stockTableSection = stockTable[:shownMonths]
    stockTableSection = stockTableSection.round(2)
    stockTableHtml = stockTableSection.to_html()

    return render(request, "pages/game.html", {"stockActions": stockActions, "stockTable": stockTableHtml})

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