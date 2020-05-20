from django.urls import path

from . import views


app_name = 'leds'
urlpatterns = [ 
    path('', views.index, name='index'),
    path('colors/', views.all_colors, name='all_colors'),
    path('colors/<color_name>/', views.color, name='color'),
]