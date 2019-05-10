from django.shortcuts import render, reverse
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from .models import Pesticide
from .config import config

import json


def index(request):
    context = {
    'message' : 'Oh dear'
    }
    return render(request, 'rup/index.html/', context)

def polygon(request):
    datas = Pesticide.objects.order_by('use')
    pesticides=[]
    uses = []
    
    for i in range(1, (len(datas))):
        if datas[i].use != None:
            if datas[i].use != datas[i-1].use:
                uses.append(datas[i])

    context = {
        'uses': uses,
        'datas' : datas,

        'SECRET_KEY_GOOGLE': config['SECRET_KEY_GOOGLE']
    }

    return render(request, 'rup/polygon.html', context)

def farmView(request):
    context = {
    'SECRET_KEY_GOOGLE': config['SECRET_KEY_GOOGLE']
    }

    return render(request, 'rup/farmView.html/', context)


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
