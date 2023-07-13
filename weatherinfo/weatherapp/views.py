from django.shortcuts import render
import requests
from datetime import timedelta,datetime
from django.core.cache import cache 
from .models import City,Coordinate
from .forms  import CityForm,CoordinateForm
# Create your views here.


def city_forecast(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=becfafca3d852ad367a137212613044f'

    
    if request.method=='POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city=form.cleaned_data['name']
            cache.set('city',city,5)
            city_name = City.objects.filter(name=city).first()
            
            if city_name == None  :
                data=City(name=city)
                data.save()
            else:
                pass    
        


    citys=cache.get('city')
    cities = City.objects.filter(name=citys)

    form = CityForm()

    weather_data  = []        

    for city in cities:
        city_weather=requests.get(url.format(city.name)).json()
        if city_weather != None:
            weather = {
                   'id':city_weather['id']
    
            }
    
            weather_data.append(weather)


    context = {
        'weather_data' : weather_data,'form': form
    }    

    return render(request,'city_forecast.html',context)
























def current_forecast(request):

    url = 'https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&units=metric&appid=becfafca3d852ad367a137212613044f'


    if request.method=='POST':
        form = CoordinateForm(request.POST)
        if form.is_valid():
            lat=form.cleaned_data['lat']
            long=form.cleaned_data['long']
            cache.set('lat',lat,2)
            cache.set('long',long,2)
            lattitude= Coordinate.objects.filter(lat=lat).first() 
            longitude=Coordinate.objects.filter(long=long).first() 
            if lattitude == None and longitude == None :
                data=Coordinate(lat=lat,long=long)
                
                data.save()
            else:
                pass    


    lat=cache.get('lat')
    long=cache.get('long')
    loc = Coordinate.objects.filter(lat=lat) & Coordinate.objects.filter(long=long) 
    form = CoordinateForm()

    weather_data  = []        

    for loc in loc:
        if loc:
            city_weather=requests.get(url.format(loc.lat,loc.long)).json()

    
            weather = {
            
                'id':city_weather['id'],
    
            }
    
        weather_data.append(weather)


    context = {
        'weather_data' : weather_data,'form': form
    }    

    return render(request,'current_forecast.html',context )











def daily_forecast(request):
   
    url = 'https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&units=metric&appid=becfafca3d852ad367a137212613044f'


    if request.method=='POST':
        form = CoordinateForm(request.POST)
        if form.is_valid():
            lat=form.cleaned_data['lat']
            long=form.cleaned_data['long']
            cache.set('lat',lat,2)
            cache.set('long',long,2)
            lattitude= Coordinate.objects.filter(lat=lat).first() 
            longitude=Coordinate.objects.filter(long=long).first() 
       
            if lattitude == None and longitude == None :
                data=Coordinate(lat=lat,long=long)
                
                data.save()
            else:
                pass    


    lat=cache.get('lat')
    long=cache.get('long')
    loc = Coordinate.objects.filter(lat=lat) & Coordinate.objects.filter(long=long) 
    form = CoordinateForm()

    weather_data  = []        

    for loc in loc:
        if loc:
            city_weather=requests.get(url.format(loc.lat,loc.long)).json()
    
            weather = {
            
                'id':city_weather ['id'],
    
            }
    
            weather_data.append(weather)


    context = {
        'weather_data' : weather_data,'form': form
    }    

    return render(request,'daily_forecast.html',context )


