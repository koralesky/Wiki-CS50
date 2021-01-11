from django.urls import path

from . import views

urlpatterns = [
    path("wiki/", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("new_page", views.new_page, name="new_page"),
    path("random", views.random_page, name="random_page"),
    path("search", views.search, name="search")
]
