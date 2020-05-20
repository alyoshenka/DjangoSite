from django.shortcuts import get_object_or_404, render

from .models import Color


def index(request):
    return render(request, 'leds/Index.html', None)

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