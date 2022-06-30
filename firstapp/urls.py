from django.urls import path

from .views import add, div, index, mul, sub

urlpatterns = [
    path("", index, name="index_page"),
    path("add/", add, name="add_page"),
    path("sub/", sub, name="sub_page"),
    path("mul/", mul, name="mul_page"),
    path("div/", div, name="div_page"),
]
