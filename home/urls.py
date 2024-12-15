from django.urls import path
from . import views

urlpatterns = [
    path('hi/', views.index, name='index'),
]