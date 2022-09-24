from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index),
    path('send_resume', views.send_resume)
]
