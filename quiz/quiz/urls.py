from django.contrib import admin
from django.urls import path,include
#from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('quiz/',include("question.url"))
]