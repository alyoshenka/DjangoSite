from django.shortcuts import get_object_or_404, render

from .models import Color, Board


def index(request):
    board = Board()
    arr = board.display_arr()
    all_colors = Color.objects.all()
    context = { 
        'board': board,
        'arr': arr,
        'colors': all_colors,
     }
    return render(request, 'leds/index.html', context)

def color(request, color_name):
    color = get_object_or_404(Color, label=color_name)
    context = {
        'color': color
    }
    return render(request, 'leds/color.html', context)

def all_colors(request):
    all_colors = Color.objects.all()
    context = {
        'all_colors': all_colors
    }
    return render(request, 'leds/all_colors.html', context)