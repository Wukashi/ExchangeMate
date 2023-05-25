from django.http import HttpResponse
from django.shortcuts import render


def starting_page(request):
    return render(request, "ExchangeMate/index.html")


def login(request):
    return render(request, "ExchangeMate/login.html")


def create_account(request):
    return render(request, "ExchangeMate/createAccount.html")


def home(request):
    return render(request, "ExchangeMate/home.html")


def deposit(request):
    return render(request, "ExchangeMate/deposit.html")


def deposit_currency(request, slug):
    currencies = {
        "zloty": "Złoty",
        "dollar": "Dollar",
        "euro": "Euro",
        "pound": "Pound"
    }

    if slug in currencies:
        currency_name = currencies[slug]
        return render(request, "ExchangeMate/deposit_currency.html", {"currency": currency_name})
    else:
        return HttpResponse("Invalid currency")


def withdraw(request):
    return render(request, "ExchangeMate/withdraw.html")


def withdraw_currency(request, slug):
    currencies = {
        "zloty": "Złoty",
        "dollar": "Dollar",
        "euro": "Euro",
        "pound": "Pound"
    }

    if slug in currencies:
        currency_name = currencies[slug]
        return render(request, "ExchangeMate/deposit_currency.html", {"currency": currency_name})
    else:
        return HttpResponse("Invalid currency")


def exchange(request):
    return render(request, "ExchangeMate/exchange.html")


def exchange_currency(request, slug):
    currencies = {
        "zloty": "Złoty",
        "dollar": "Dollar",
        "euro": "Euro",
        "pound": "Pound"
    }

    if slug in currencies:
        currency_name = currencies[slug]
        return render(request, "ExchangeMate/exchange_currency.html", {"currency": currency_name, "slug": slug})
    else:
        return HttpResponse("Invalid currency")



def logout(request):
    pass