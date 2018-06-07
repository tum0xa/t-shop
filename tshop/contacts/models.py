from django.db import models


class Company(models.Model):
    name = models.CharField(default="NoName", max_length=255, blank=False)
    phone = models.CharField(default="+7 000 000 00 00", max_length=20)
    email = models.EmailField(default="mail@mail.ru", max_length=255)
    noreply_email = models.EmailField(default="mail@mail.ru", max_length=255)
