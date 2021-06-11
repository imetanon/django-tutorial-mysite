from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home), #appdb/home/
    path('test/', views.test), #appdb/test/
    path('index/', views.index), #appdb/test/
]