from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

import json

from .models import Color, Board, LED


def index(request):
    """Homepage"""

    all_colors = Color.objects.all() # change to selected colors
    all_boards = Board.objects.all() # change to selected boards

    try:
        current_color_label = request.session['current_color']
    except:
        current_color_label = None

    try:
        current_board_label = request.session['current_board']
        current_board = Board.objects.get(label=current_board_label)
        current_arr = current_board.display_arr()
    except:
        current_board = None
        current_arr = None

    context = { 
        'current_arr': current_arr,
        'colors': all_colors,
        'boards': all_boards,
        'current_color': current_color_label,
        'current_board': current_board
     }
    return render(request, 'leds/index.html', context)

def color(request, color_name):
    """Displays information for a given color"""
    color = get_object_or_404(Color, label=color_name)
    context = {
        'color': color
    }
    return render(request, 'leds/color.html', context)

def board(request, board_label):
    """Displays information for a given board"""
    board = get_object_or_404(Board, label=board_label)
    arr = board.display_arr()
    context = { 'board': board, 'arr': arr }
    return render(request, 'leds/board.html', context)

def all_colors(request):
    """Show all the colors"""
    all_colors = Color.objects.all()    
    context = {
        'all_colors': all_colors
    }
    return render(request, 'leds/all_colors.html', context)

def all_boards(request):
    """Show all boards"""
    all_boards = Board.objects.all()
    context = { 'all_boards': all_boards }
    return render(request, 'leds/all_boards.html', context)

def set_led_color(request, board_label, led_idx, color_label):

    board = Board.objects.get(label=board_label)
    led = board.leds[led_idx]
    color = Color.objects.get(label=color_label)

    led.color = color
    led.save()

    return HttpResponseRedirect(reverse('leds:boards', args=(board_label,)))


# session testing

def selected_color(request):
    """Get selected color from session"""
    _label = request.session['current_color']
    color = None if _label == 'none' else Color.objects.get(label=_label)
    return color


def LED_click(request, led_index):
    """An LED in a board is clicked
        set LED color"""
    # get selected color
    # find associated color by label
    color = selected_color(request)
    # get currently displayed board in session
    try:
        board_label = request.session['current_board']
        board = Board.objects.get(label=board_label)
    except:
        board = None
        
    if color is not None and board is not None:
        # find LED associated to button (by idx)
        #   and board
        led = LED.objects.get(index=led_index, board=board)
        # set LED color to color
        led.color = color
        # save
        led.save()

        print('set ', led_index, ' to ', color)

    # return to original page   
    return HttpResponseRedirect(reverse('leds:index'))

def color_click(request, color_label):
    """A displayed color is clicked
        select color"""
    color = Color.objects.get(label=color_label)
    obj = json.loads(color.json())[0]
    label = obj.get('fields').get('label')

    if not 'current_color' in request.session:
        request.session['current_color'] = 'none'
    elif request.session['current_color'] == label:
        request.session['current_color'] = 'none'
    else:
        request.session['current_color'] = label

    # return HttpResponse(request.session['current_color'])
    return HttpResponseRedirect(reverse('leds:index'))

def board_click(request, board_label):
    """A displayed board is clicked
        select board"""
    board = Board.objects.get(label=board_label)
    obj = json.loads(board.json())[0]
    label = obj.get('fields').get('label')

    if not 'current_board' in request.session:
        request.session['current_board'] = 'none'
    elif request.session['current_board'] == label:     
        request.session['current_board'] = 'none'
    else:
        request.session['current_board'] = label

    #return HttpResponse(request.session['current_board'])
    return HttpResponseRedirect(reverse('leds:index'))
