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
    index = models.IntegerField()
    color = models.ForeignKey(
        Color, on_delete=models.CASCADE,
    )