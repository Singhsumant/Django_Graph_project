
from django.db import models


class schoolModel(models.Model):
    district_name = models.CharField(max_length=255)
    category = models.CharField(max_length=50)
    language = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.district_name} - {self.category} ({self.language})"
