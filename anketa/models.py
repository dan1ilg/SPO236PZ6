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

class Myuser(User):
    phonenumber = models.TextField(max_length=50, verbose_name="Номер телефона")

    class Meta:
        ordering = ["-title"]
        verbose_name = "Гражданин"
        verbose_name_plural = "Граждане"

    def __str__(self):
        return self.title

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Myuser._meta.fields]

class Vopros(models.Model):
    textvopr = models.TextField(max_length=50, verbose_name="Текст вопроса")
    ball = models.IntegerField(default=0, verbose_name="Балл")
    naviki = models.ForeignKey(Naviki, on_delete=models.CASCADE, ralated_name='voprosnaviki')

    class Meta:
         ordering = ["-title"]
         verbose_name = "Вопрос"
         verbose_name_plural = "Вопросы"

    def __str__(self):
        return self.title

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Vopros._meta.fields]


class PystoiSertificat(models.Model):
    textvopr = models.TextField(max_length=50, verbose_name="Текст вопроса")
    ball = models.IntegerField(default=0, verbose_name="Балл")
    naviki = models.ForeignKey(Naviki, on_delete=models.CASCADE, ralated_name='voprosnaviki')

    class Meta:
        ordering = ["-title"]
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    def __str__(self):
        return self.title

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Vopros._meta.fields]