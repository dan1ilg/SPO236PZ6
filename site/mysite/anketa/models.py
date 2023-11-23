from django.contrib.auth.models import User
from django.db import models

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
        verbose_name_plural = "Навык"

    def __str__(self):
        return self.title

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Naviki._meta.fields]

class Myuser(User):
    title = models.TextField(max_length=50, verbose_name="Пользователь")
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
    title = models.TextField(max_length=50, verbose_name="Текст вопроса")
    ball = models.IntegerField(default=0, verbose_name="Балл")
    naviki = models.ForeignKey(Naviki, on_delete=models.CASCADE, related_name='voprosnaviki')

    class Meta:
         ordering = ["-title"]
         verbose_name = "Вопрос"
         verbose_name_plural = "Вопросы"

    def __str__(self):
        return self.title

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Vopros._meta.fields]


class PystoiSertificat(models.Model):
    title = models.TextField(max_length=50, verbose_name="Название сертификата")
    full = models.ImageField(upload_to='PystoiSertificat/%Y/%m/%d', blank=True)
    one = models.ImageField(upload_to='PystoiSertificat/%Y/%m/%d', blank=True)

    class Meta:
        ordering = ["-title"]
        verbose_name = "Пустой сертификат"
        verbose_name_plural = "Пустые сертификаты"

    def __str__(self):
        return self.title

    def get_fields(self):
        return [(field.name, field.value_to_string(self))
                for field in PystoiSertificat._meta.fields]


class Model_prof(models.Model):
    title = models.TextField(max_length=50, verbose_name="Название")
    Proffessia = models.ForeignKey(Proffessia, on_delete=models.PROTECT, verbose_name="Профессия")
    Naviki = models.ForeignKey(Naviki, on_delete=models.PROTECT, verbose_name="Навык")
    ball = models.PositiveIntegerField()

    class Meta:
        ordering = ["-title"]
        verbose_name = "Модельная профессия"
        verbose_name_plural = "Модельные профессии"

    def __str__(self):
        return self.title

    def get_fields(self):
        return [(field.name, field.value_to_string(self))
                for field in Model_prof._meta.fields]