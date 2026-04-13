from django.urls import path
from . import views

urlpatterns = [
    path("myfirst/", views.myfirst, name="myfirst"),
]