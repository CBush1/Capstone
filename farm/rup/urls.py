from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name ='rup'
urlpatterns = [
    path('', views.index, name='index'),
    path('polygon/', views.polygon, name='polygon'),
    path('save_product/', views.save_product, name='save_product'),
    path('get_product/', views.get_product, name='get_product'),
    path('mylogin/', views.mylogin, name='mylogin'),
    path('modal/', views.modal, name='modal'),
    # path('locations/', views.locations, name='locations'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
