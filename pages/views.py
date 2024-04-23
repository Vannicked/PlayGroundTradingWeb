from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import stockActions
from .models import Portfolio

import pandas as pd

def home(request):
    return render(request, "pages/home.html", {})

def game(request):

    stockTable = pd.read_csv('pages/static/pages/StockPrices.csv')
    shownMonths = 7
    stockTableSection = stockTable[:shownMonths]
    stockTableSection = stockTableSection.round(2)
    stockTableHtml = stockTableSection.to_html()

    if request.method == "POST":
        stockActionsForm = stockActions(request.POST)

        if 'buy_stock' in request.POST:
            if stockActionsForm.is_valid():
                p = Portfolio.objects.all()[0]
                boughtStock = stockActionsForm.cleaned_data['stock'].lower()
                sharesBought = stockActionsForm.cleaned_data['shares']
                checkStock(p, boughtStock, sharesBought)
                p.save()
                updateStockValues(p, shownMonths)
                print("You have bought a stock!")
        elif 'sell_stock' in request.POST:
            if stockActionsForm.is_valid():
                p = Portfolio.objects.all()[0]
                soldStock = stockActionsForm.cleaned_data['stock'].lower()
                sharesSold = -abs(stockActionsForm.cleaned_data['shares'])
                checkStock(p, soldStock, sharesSold)
                p.save()
                updateStockValues(p, shownMonths)
                print("You have sold a stock!")
    else:
        x = Portfolio.objects.count() 
        if x < 1:
            p = Portfolio(aal=0, aapl=0, amzn=0, bac=0, dal=0, hmc=0, jnj=0, jpm=0, lly=0, luv=0, msft=0, tm=0, tsla=0, unh=0, v=0, totalValue=0)
            p.save()
        stockActionsForm = stockActions()

    playerPortfolio = Portfolio.objects.filter(id=1).values()

    return render(request, "pages/game.html", {"stockActions": stockActions, "stockTable": stockTableHtml, "playerPortfolio": playerPortfolio})

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
    elif (stock_name == 'v'):
        p.v = p.v + num_shares
    else:
        print("yikes!")

def updateStockValues(p, monthIndex):
    stockValues = pd.read_csv("pages/static/pages/StockPrices.csv")
    monthIndex = monthIndex - 1
    aalValue = p.aal * stockValues.iat[monthIndex, 1]
    aaplValue = p.aapl * stockValues.iat[monthIndex, 2]
    amznValue = p.amzn * stockValues.iat[monthIndex, 3]
    bacValue = p.bac * stockValues.iat[monthIndex, 4]
    dalValue = p.dal * stockValues.iat[monthIndex, 5]
    hmcValue = p.hmc * stockValues.iat[monthIndex, 6]
    jnjValue = p.jnj * stockValues.iat[monthIndex, 7]
    jpmValue = p.jpm * stockValues.iat[monthIndex, 8]
    llyValue = p.lly * stockValues.iat[monthIndex, 9]
    luvValue = p.luv * stockValues.iat[monthIndex, 10]
    msftValue = p.msft * stockValues.iat[monthIndex, 11]
    tmValue = p.tm * stockValues.iat[monthIndex, 12]
    tslaValue = p.tsla * stockValues.iat[monthIndex, 13]
    unhValue = p.unh * stockValues.iat[monthIndex, 14]
    vValue = p.v * stockValues.iat[monthIndex, 15]
    p.totalValue = round(aalValue + aaplValue + amznValue + bacValue + dalValue + hmcValue + jnjValue + jpmValue + llyValue + luvValue + msftValue + tmValue + tslaValue + unhValue + vValue, 2)
    p.save()