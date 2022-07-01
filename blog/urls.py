from django.urls import path

from .views import blog_index_page, create, single

urlpatterns = [
    path("", blog_index_page, name="blog_index_page"),
    path("<int:id>/", single, name="single_blog_page"),
    path("create/", create),
]
