from django.shortcuts import render, reverse
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from .models import Pesticide, Location, LocationPesticide
from .config import config
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.utils import timezone


import json
import datetime

def index(request):
    context = {
    'message' : 'Oh dear'
    }
    return render(request, 'rup/index.html/', context)

def mylogin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        if user.is_staff:
            return HttpResponseRedirect(reverse('rup:polygon'))
        elif user.is_active:
            return HttpResponseRedirect(reverse('rup:user_view'))
    # else:
        # Return a 'disabled account' error message
            ...
    # else:
    #     # Return an 'invalid login' error message.

@login_required
def polygon(request):
    datas = Pesticide.objects.order_by('use')
    locations = Location.objects.all()
    uses = []
    for i in range(1, (len(datas))):
        if datas[i].use != None:
            if datas[i].use != datas[i-1].use:
                uses.append(datas[i])

    context = {
        'uses': uses,
        'datas' : datas,
        'locations':locations,
        'SECRET_KEY_GOOGLE': config['SECRET_KEY_GOOGLE'],
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
    modal_data = LocationPesticide(location_id=location_id, pesticide_id=pesticide_id, start=start, end=end, user=user)
    modal_data.save()

    return HttpResponse('ok')

@login_required
def user_view(request):
    # events = LocationPesticide.objects.prefetch_related('pesticide', 'user', 'location')
    now = timezone.now()
    events = LocationPesticide.objects.filter(start__lte=now, end__gte=now)
    locations = Location.objects.all()

    context = {
        'events': events,
        'locations': locations,
        'SECRET_KEY_GOOGLE': config['SECRET_KEY_GOOGLE'],
    }
    print(events)
    return render(request, 'rup/user_view.html', context)
