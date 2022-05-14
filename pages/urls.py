from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.view),
    path('about',views.about),
    path('services',views.services),
    path('contact',views.contact),
]
