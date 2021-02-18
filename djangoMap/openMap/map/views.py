from django.shortcuts import render
from django.http import HttpResponse

from .models import *
from .serializers import *
from .forms import *

from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
import json
import pgeocode

# Create your views here.
class CityView(viewsets.ModelViewSet):
    queryset = my_cities.objects.all()
    serializer_class = MyCitySerializer
 
class LatLongView(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    queryset = my_latlong.objects.all()
    serializer_class = MyLatLongSerializer
    filter_fields = ['city']



@api_view(['POST'])
def data_from_zip(request):
    if request.method == "POST":
        try:
            country_code = request.data.get("country_code")
            pincode = request.data.get("pincode")
            nomi = pgeocode.Nominatim(country_code)
            res = nomi.query_postal_code(pincode)
            return HttpResponse(res.to_json(), content_type='application/json')
        except Exception as e:
            content = {"message":f"{e}"}
            return HttpResponse(json.dumps(content), status=203)


def viewmap(request):
    form = CityForm
    if request.method == "POST":
        data = request.POST.get("City")
        content = {'loc':data, 'form':form}
        return render(request, 'map.html', content)
    content = {'loc':'current_location', 'form':form}
    return render(request, 'map.html', content)

def showpolygon(request):
    return render(request,'polygon.html')
    

def search_map(request):
    return render(request, 'search_map2.html')

def sub_search(request):
    return render(request,'search_in_search.html')

def search_mymap(request):
    return render(request,'open_street_map.html')
    
def showgis(request):
    return render(request,'ARCGIRS.html')
    
def arcgisdemo(request):
    return render(request,'arcgisdemo2.html')