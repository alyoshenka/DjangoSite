from django.db import models


class Color(models.Model):
    label = models.CharField(default="no_label", max_length=20)
    r = models.PositiveSmallIntegerField(default=0)
    g = models.PositiveSmallIntegerField(default=0)
    b = models.PositiveSmallIntegerField(default=0)
    a = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.label + " (" \
            + str(self.r) + "," + str(self.g) \
            + "," + str(self.b) + "," \
            + str(self.a) + ")"

class LED(models.Model):
    index = models.IntegerField(default=0)
    color = models.ForeignKey(
        Color, on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.index

    def color_style(self):
        return "--color: " + self.color.label + ";"

class Board(models.Model):
    height = models.PositiveSmallIntegerField(default=8)
    width = models.PositiveSmallIntegerField(default=32)
    label = models.CharField(default="board", max_length=30)

    def __init__(self):
        super().__init__()
        self.leds = []
        for i in range(self.width * self.height):
            self.leds.append(LED(index=i))

    def size(self):
        return self.width * self.height

    def display_arr(self):
        ret = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                idx = x * self.height + y
                row.append(self.leds[idx])
            ret.append(row)
        return ret

    def divisible_by_height(self, num):
        return num % self.height == 0

    def led(self, idx):
        return self.leds[idx]