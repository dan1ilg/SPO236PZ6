from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static

from mysite.anketa.views import *
from mysite.home import views
app_name = 'anketa'
urlpatterns = [
    path('proffessia/', ProffessiaView.as_view(), name='Proffessia'),
    path('proffessia/update/<int:pk>/', ProffessiaUpdate.as_view(), name='ProffessiaUpdate'),
    path('proffessia/detail/<int:pk>/', ProffessiaDetail.as_view(), name='ProffessiaDetail'),
    path('proffessia/create/', ProffessiaCreate.as_view(), name='ProffessiaCreate'),
    path('proffessia/delete/<int:pk>/', ProffessiaDelete.as_view(), name='ProffessiaDelete'),

    path('naviki/', NavikiView.as_view(), name='Naviki'),
    path('naviki/update/<int:pk>/', NavikiUpdate.as_view(), name='NavikiUpdate'),
    path('naviki/detail/<int:pk>/', NavikiDetail.as_view(), name='NavikiDetail'),
    path('naviki/create/', NavikiCreate.as_view(), name='NavikiCreate'),
    path('naviki/delete/<int:pk>/', NavikiDelete.as_view(), name='NavikiDelete'),

    path('vopros/', VoprosView.as_view(), name='Vopros'),
    path('vopros/update/<int:pk>/', VoprosUpdate.as_view(), name='VoprosUpdate'),
    path('vopros/detail/<int:pk>/', VoprosDetail.as_view(), name='VoprosDetail'),
    path('vopros/create/', VoprosCreate.as_view(), name='VoprosCreate'),
    path('vopros/delete/<int:pk>/', VoprosDelete.as_view(), name='VoprosDelete'),    

    path('pystoisertificat/', PystoiSertificatView.as_view(), name='PystoiSertificat'),
    path('pystoisertificat/update/<int:pk>/', PystoiSertificatUpdate.as_view(), name='PystoiSertificatUpdate'),
    path('pystoisertificat/detail/<int:pk>/', PystoiSertificatDetail.as_view(), name='PystoiSertificatDetail'),
    path('pystoisertificat/create/', PystoiSertificatCreate.as_view(), name='PystoiSertificatCreate'),
    path('pystoisertificat/delete/<int:pk>/', PystoiSertificatDelete.as_view(), name='PystoiSertificatDelete'),

    path('model_prof/', Model_profView.as_view(), name='Model_prof'),
    path('model_prof/update/<int:pk>/', Model_profUpdate.as_view(), name='Model_profUpdate'),
    path('model_prof/detail/<int:pk>/', Model_profDetail.as_view(), name='Model_profDetail'),
    path('model_prof/create/', Model_profCreate.as_view(), name='Model_profCreate'),
    path('model_prof/delete/<int:pk>/', Model_profDelete.as_view(), name='Model_profDelete'),    
]
