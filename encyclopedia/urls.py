from django.urls import path

from . import views

urlpatterns = [
    path("wiki/", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("add_new_page", views.new_page, name = "new_page"),
]
