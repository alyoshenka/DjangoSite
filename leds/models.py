from django.db import models
from django.core import serializers


class Color(models.Model):
    label = models.CharField(default="no_label", max_length=20)
    r = models.PositiveSmallIntegerField(default=0)
    g = models.PositiveSmallIntegerField(default=0)
    b = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.label + " (" \
            + str(self.r) + "," + str(self.g) \
            + "," + str(self.b) + ")"

    def json(self):
        dat = serializers.serialize("json", [self])
        return dat

class LED(models.Model):
    index = models.IntegerField(default=0)
    color = models.ForeignKey(
        Color, on_delete=models.CASCADE,
    )

    def __str__(self):
        return str(self.index)

    def json(self):
        dat = serializers.serialize("json", [self])
        return dat

    def color_style(self):
        return "--color: " + self.color.label + ";"

class Board(models.Model):
    height = models.PositiveSmallIntegerField(default=8)
    width = models.PositiveSmallIntegerField(default=32)
    label = models.CharField(default="board", max_length=30)
    leds = models.ManyToManyField(LED)

    def __str__(self):
        return self.label

    def json(self):
        dat = serializers.serialize("json", [self])
        return dat

    def show_leds(self):
        for led in self.leds.all():
            print(led.index)

    def size(self):
        return self.width * self.height

    def display_arr(self):
        ret = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                idx = x * self.height + y
                row.append(self.leds.get(index=idx))
            ret.append(row)
        return ret

    def divisible_by_height(self, num):
        return num % self.height == 0

    def led(self, idx):
        return self.leds[idx]