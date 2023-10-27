from django.contrib import admin
from .models import *


# Register your models here.
class ProfessiaAdmin(admin.ModelAdmin):
    list_display = ['title']
admin.site.register(Professia, ProfessiaAdmin)

class NavikiAdmin(admin.ModelAdmin):
    list_display = ['title']
admin.site.register(Naviki, NavikiAdmin)

class VoprosAdmin(admin.ModelAdmin):
    list_display = ['textvopr', 'ball', 'naviki']
admin.site.register(Vopros, VoprosAdmin)

class Model_profAdmin(admin.ModelAdmin):
    list_display = ['title', 'Professia', 'Naviki','ball']
admin.site.register(Model_prof, Model_profAdmin)

class PystoiSertificatAdmin(admin.ModelAdmin):
    list_display = ['title', 'full', 'one']
admin.site.register( PystoiSertificat, PystoiSertificatAdmin)

class MyuserAdmin(admin.ModelAdmin):
    list_display = ['phonenumber']
admin.site.register( Myuser, MyuserAdmin)