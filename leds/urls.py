from django.urls import path

from . import views


app_name = 'leds'
urlpatterns = [ 
    path('', views.index, name='index'),
    path('colors/', views.all_colors, name='all_colors'),
    path('boards/', views.all_boards, name='all_boards'),

    path('colors/<color_name>/', views.color, name='color'),
    path('boards/<board_label>/', views.board, name='board'),

    path('LED_click/<int:led_index>/', views.LED_click, name='LED_click'),
    path('colorClick/<color_label>/', views.color_click, name='color_click'),
    path('boardClick/<board_label>/', views.board_click, name='board_click')
]