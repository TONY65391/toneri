from django.urls import path
from PERSONAL import views

urlpatterns = [
    path('', views.test),
]