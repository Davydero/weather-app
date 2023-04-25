from django.shortcuts import render
import json #la respuesta de la API sera en formato json
import urllib.request

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city'] #este es el valor leido desde el html
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=911b46760b903837fd9db7cfedfab285').read() #llamada  a la API
        json_data = json.loads(res)
        data = { #Toda la informacion que sacamos de la respuesta de la API en un diccionario
            "country_code": str(json_data['sys']['country']),
            "coordinate" : str(json_data['coord']['lon'])+' '+str(json_data['coord']['lat']),
            "temp" : str(json_data['main']['temp'])+' k',
            "pressure" : str(json_data['main']['pressure']),
            "humidity" : str(json_data['main']['humidity'])
        } 

    else:
        city = ''
        data = {}
    return render(request, 'index.html', {'city':city, 'data':data})