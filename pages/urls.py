from django.urls import path
from . import views

urlpatterns = [
    path('',views.view,name='home'),
    path('about',views.about),
    path('services',views.services),
]
