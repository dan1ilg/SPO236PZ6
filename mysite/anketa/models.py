from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Proffessia(models.Model):
    title = models.TextField(max_length=50, verbose_name="Профессия")

    class Meta:
        ordering = ["-title"]
        verbose_name = "Профессия"
        verbose_name_plural = "Профессии"

    def __str__(self):
        return self.title

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Proffessia._meta.fields]


class Naviki(models.Model):
    title = models.TextField(max_length=50, verbose_name="Навыки")

    class Meta:
        ordering = ["-title"]
        verbose_name = "Навыки"
        verbose_name_plural = "Навыки"

    def __str__(self):
        return self.title

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Naviki._meta.fields]

