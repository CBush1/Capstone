
from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('', views.index, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login, {'template_name': 'login.html'}, name='login'),
    path('logout/', views.logout, {'next_page': 'login'}, name='logout'),
    path('register/', views.register, name='register'),
]
