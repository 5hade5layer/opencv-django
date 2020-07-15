from django.urls import path

from . import views

urlpatterns = [
    path('', views.home.as_view(), name='home'),
    path('trange/', views.trange, name='trange'),
    path('result/', views.result, name='result') 
]