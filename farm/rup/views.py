from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from .models import Pesticide, Location, LocationPesticide, UserProfile
from django.contrib.auth.models import User

from .config import config
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.utils import timezone

import json
import datetime
import pytz

# def signup(request):
#     return render(request, 'registration/signup.html')


def mylogin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        # if user.is_active:
        if user.is_active:
            return redirect('rup:newfarm.html')
        elif UserProfile.user == user.get_username(self):
            return redirect('rup:user_view')
    # else:
        # Return a 'disabled account' error message
            ...
    else:
        alert('invalid login')


def set_timezone(request):
    if request.method == 'POST':
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('/')
    else:
        return render(request, 'user_view.html', {'timezones': pytz.common_timezones})


def newfarm(request):
    context = {
        'SECRET_KEY_GOOGLE': config['SECRET_KEY_GOOGLE']
    }
    return render(request, 'rup/newfarm.html', context)


@login_required
def polygon(request):
    current_user = request.user
    datas = Pesticide.objects.order_by('use')
    locations = Location.objects.all()
    user_name = User.objects.get(pk=current_user.pk)
    users = UserProfile.objects.filter(user=user_name)

    latlngs = {
        'lat': users[0].lat,
        'lng': users[0].lng
    }

    uses = []
    for i in range(1,(len(datas))):
        if datas[i].use != None:
            if datas[i].use != datas[i-1].use:
                uses.append(datas[i])

    context = {
        'uses':uses,
        'datas':datas,
        'latlngs': latlngs,
        'locations':locations,
        'SECRET_KEY_GOOGLE':config['SECRET_KEY_GOOGLE'],
    }
    return render(request, 'rup/polygon.html', context)


def get_product(request):
    data_num = 0
    data = {'products' : []}
    pesticides = Pesticide.objects.all()
    for pesticide in pesticides:
        data['products'].append({
            'product_name':pesticide.product_name,
            'rui':pesticide.rui,
            'rei':pesticide.rei,
            'use':pesticide.use,
            'epa_number':pesticide.epa_number,
        })
        data_num += 1

    return JsonResponse(data)


def modal(request):
    data = json.loads(request.body)
    location_id = data['location_id']
    pesticide_id = data['pesticide_id']
    user = request.user
    start = data['start']
    end = data['end']
    rate = data['rate']
    target = data['target']
    applicator = data['applicator']
    modal_data = LocationPesticide(location_id=location_id, pesticide_id=pesticide_id, start=start, end=end, user=user, rate=rate, target=target, applicator=applicator)
    modal_data.save()

    return HttpResponse('ok')

def create_location(request):
    data = json.loads(request.body)
    print(data)
    # user = request.user
    # polyname = data['polyname']
    # rectBounds = data['rectBounds']
    # polyList = data['polyList']
    # newLat = data['centerLat']
    # newLng = data['centerLng']
    # areaRect = data['areaRect']
    # areaPoly = data['areaPoly']
    #
    # location_data = Location(polyname=polyname, rectBounds=rectBounds, polyList=polyList, centerLat=centerLat, centerLng=centerLng, areaRect=areaRect, areaPoly=areaPoly)
    # location_data.save()
    # print(location_data)

    return HttpResponse('ok')


def pick_center(request):
    data = json.loads(request.body)
    lat = data['lat']
    lng = data['lng']
    user = request.user
    user_center = UserProfile(lat=lat, lng=lng, user=user)
    user_center.save()

    return HttpResponse('ok')



def user_view(request):
    # events = LocationPesticide.objects.prefetch_related('pesticide', 'user', 'location')
    now = timezone.now()
    # print(now)
    events = LocationPesticide.objects.filter(start__lte=now, end__gte=now)
    locations = Location.objects.all()

    context = {
        'events': events,
        'locations': locations,
        'SECRET_KEY_GOOGLE': config['SECRET_KEY_GOOGLE'],
    }
    return render(request, 'rup/user_view.html', context)
