from django.urls import path
from . import views #importamos todas las funcioines definidas en views

urlpatterns = [
    path('', views.index, name='index')
]