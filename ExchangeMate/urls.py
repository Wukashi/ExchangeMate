"""
URL configuration for ExchangeMate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from ExchangeMate import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.starting_page, name="startPage"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("createaccount", views.create_account, name="createAccount"),
    path("home", views.home, name="home"),
    path("deposit", views.deposit, name="deposit"),
    path("deposit/<slug>", views.deposit_currency, name="depositCurrency"),
    path("withdraw", views.withdraw, name="withdraw"),
    path("withdraw/<slug>", views.withdraw_currency, name="withdrawCurrency"),
    path("exchange", views.exchange, name="exchange"),
    path("exchange/<slug>", views.exchange_currency, name="exchangeCurrency")
]
