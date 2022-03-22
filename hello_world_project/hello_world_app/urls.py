from django.urls import path
from . import views

urlpatterns = [
    path('hello_world/',views.index)
]