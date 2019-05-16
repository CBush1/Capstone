from django.shortcuts import render, reverse
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from .models import Pesticide, Location, LocationPesticide
from .config import config
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

import json

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
        # if user.is_active:
        login(request, user)
        return HttpResponseRedirect(reverse('rup:polygon'))
    #     else:
    #         # Return a 'disabled account' error message
    #         ...
    # else:
    #     # Return an 'invalid login' error message.

@login_required
def polygon(request):
    datas = Pesticide.objects.order_by('use')
    locations = Location.objects.all()
    spray_locations = LocationPesticide.objects.all()
    pesticides=[]
    uses = []
    polygons = []

    for i in range(1, (len(datas))):
        if datas[i].use != None:
            if datas[i].use != datas[i-1].use:
                uses.append(datas[i])

    context = {
        'uses': uses,
        'datas' : datas,
        'locations':locations,
        'spray_locations':spray_locations,
        'SECRET_KEY_GOOGLE': config['SECRET_KEY_GOOGLE'],
    }

    return render(request, 'rup/polygon.html', context)

def save_product(request):
    data = json.loads(request.body)
    product_name = data['product_name']
    epa_number = data['epa_number']
    rui = data['rui']
    rei = data['rei']
    product = Pesticide(product_name=product_name, epa_number=epa_number, rui=rui, rei=rei)
    product.save()
    return HttpResponse('ok')

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
    print(data)
    product_name = data['product']
    use = data['use']
    epa_number = data['epa_number']
    rei = data['rei_para']
    # modal_data = LocationPesticide(product_name=product_name, epa_number=epa_number, use=use, rei=rei)
    # modal_data.save()
    # print(modal_data)
    return HttpResponse('ok')
#
# def locations(request):
#     locations = Location.objects.all()
#     context = {
#         'locations':locations,
#     }
#     print(locations[2])
#
#     return render(request, 'rup/polygon.html', context)
