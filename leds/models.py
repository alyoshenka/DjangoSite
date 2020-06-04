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


class Board(models.Model):
    height = models.PositiveSmallIntegerField(default=8)
    width = models.PositiveSmallIntegerField(default=32)
    label = models.CharField(default="board", max_length=30)

    # one to many leds

    def __str__(self):
        return self.label

    def json(self):
        dat = serializers.serialize("json", [self])
        return dat

    def size(self):
        return self.width * self.height

    def display_arr(self):
        ret = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                idx = x * self.height + y
                row.append(LEDS.objects.get(board=self))
            ret.append(row)
        return ret

    def divisible_by_height(self, num):
        return num % self.height == 0

    #def led(self, idx):
        #return self.leds[idx]


class LED(models.Model):
    index = models.IntegerField(default=0)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.board.label + ":" + str(self.index)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check = models.Q(                   
                    index__gte=0
                ),
                name = "leds_LED_index_gte_0"
            )
        ]

    def json(self):
        dat = serializers.serialize("json", [self])
        return dat

    def color_style(self):
        return "--color: " + self.color.label + ";"