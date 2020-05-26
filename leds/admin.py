from django.contrib import admin

from .models import Color, LED, Board

admin.site.register(Color)
admin.site.register(LED)
admin.site.register(Board)
