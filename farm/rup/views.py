from django.shortcuts import render
from django.http import HttpResponse
from .models import Pesticide
# from django.conf import settings

# Create your views here.

def index(request):
    context = {
    'message' : 'Oh dear'
    }
    return render(request, 'rup/index.html/', context)

def polygon(request):
    # pesticide = Pesticide.objects.get(pk=product_name_id)
    context = {
    'map_message' : 'We did it!',

    # 'api_key': settings.GOOGLE_MAPS_API_KEY,
    }


    return render(request, 'rup/polygon.html/', context)
