
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import show,check
urlpatterns = [
    path('soalat/<str:name1>',show),
    path("pasokh/<str:name>/<int:id_az>",check)
]