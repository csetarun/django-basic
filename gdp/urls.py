from .views import ListCountries
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', ListCountries.as_view()),
]