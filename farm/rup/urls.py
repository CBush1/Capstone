from django.conf.urls.i18n import i18n_patterns
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name ='rup'
urlpatterns = [
    path('newfarm/', views.newfarm, name='newfarm'),
    path('polygon/', views.polygon, name='polygon'),
    path('get_product/', views.get_product, name='get_product'),
    path('mylogin/', views.mylogin, name='mylogin'),
    path('modal/', views.modal, name='modal'),
    path('user_view/', views.user_view, name='user_view'),
    path('create_location/', views.create_location, name='create_location'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
