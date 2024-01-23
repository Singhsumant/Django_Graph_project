
from django.db import models

class matchModel(models.Model):
    season = models.IntegerField()
    winner = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.season} - {self.winner}"

