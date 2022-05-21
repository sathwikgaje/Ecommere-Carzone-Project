from ast import keyword
from django.shortcuts import render,get_object_or_404
from .models import Car
from django.core.paginator import Paginator


def cars(request):
    cars = Car.objects.order_by("-created_date")
    paginator = Paginator(cars,4)
    page = request.GET.get('page')
    page_cars = paginator.get_page(page)
    models_search = Car.objects.values_list('model',flat=True).distinct()
    year_search = Car.objects.values_list('year',flat=True).distinct()
    city_search = Car.objects.values_list('city',flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style',flat=True).distinct()
    data={
        'models_search' : models_search,
        'year_search' : year_search,
        'city_search' : city_search,
        'body_style_search' : body_style_search,
        'cars' : page_cars,
    }
    return render(request,'cars/cars.html',data)

def car_detail(request,id):
    single_car = get_object_or_404(Car,pk=id)
    data={
        'single_car' : single_car
    }
    return render(request,'cars/car_detail.html',data)

def search(request):
    cars = Car.objects.order_by("-created_date")
    models_search = Car.objects.values_list('model',flat=True).distinct()
    year_search = Car.objects.values_list('year',flat=True).distinct()
    city_search = Car.objects.values_list('city',flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style',flat=True).distinct()
    transmission_search = Car.objects.values_list('transmission',flat=True).distinct()
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        cars = cars.filter(description__icontains=keyword)

    if 'model' in request.GET:
        model = request.GET['model']
        cars = cars.filter(model__iexact = model)

    if 'city' in request.GET:
        city = request.GET['city']
        cars = cars.filter(city__iexact = city)
    
    if 'year' in request.GET:
        year = request.GET['year']
        cars = cars.filter(year__iexact = year)
    
    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        cars = cars.filter(body_style__iexact = body_style)

    if 'transmission' in request.GET:
        transmission = request.GET['transmission']
        cars = cars.filter(transmission__iexact=transmission)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        cars = cars.filter(price__gte = min_price)
    
    if 'max_price' in request.GET:
        max_price = request.GET['max_price']
        cars = cars.filter(price__lte = max_price)
    
    data={
        'models_search' : models_search,
        'year_search' : year_search,
        'city_search' : city_search,
        'body_style_search' : body_style_search,
        'transmission_search' : transmission_search,
        'cars' : cars
    }
    return render(request,'cars/search.html',data)