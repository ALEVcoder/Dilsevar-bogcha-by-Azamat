from django.urls import path
from . import views
urlpatterns = [
    path('', views.HomeContact, name='home'),
    path('about/', views.About, name='about'),
    path('rasmlar/', views.Gallery, name='galery'),
    path('jamoa/', views.News, name='news'),
    path('contact/', views.Contact, name='contact'),
    
]