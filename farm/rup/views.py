from django.shortcuts import render, reverse
from django.http import HttpResponse,HttpResponseRedirect
from .models import Pesticide
# from django.conf import settings

# Create your views here.

def index(request):
    context = {
    'message' : 'Oh dear'
    }
    return render(request, 'rup/index.html/', context)

def polygon(request):

    pesticides = Pesticide.objects.all()

    context = {'pesticides' : pesticides}

    # 'api_key': settings.GOOGLE_MAPS_API_KEY,
    return render(request, 'rup/polygon.html/', context)

def selectproduct(request):
    pesticides = Pesticide.objects.all()
    context = {'pesticides' : pesticides}
    return HttpResponseRedirect(reverse('rup:polygon'))
