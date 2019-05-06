from django.conf.urls import url
from django.urls import path
from . import views

app_name ='rup'
urlpatterns = [
    path('', views.index, name='index'),
    path('polygon/', views.polygon, name='polygon'),
]
