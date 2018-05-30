from django.db import models

class Category(models.Model):
    name = models.CharField(default="Category", max_length=255, blank=False)
    active = models.BooleanField(default=True)
