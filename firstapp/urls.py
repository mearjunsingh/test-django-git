from django.urls import path

from .views import hello

urlpatterns = [path("join/", hello, name="home_page")]
