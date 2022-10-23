from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search/", views.search, name="search"),
    path("create_entry/", views.new_entry, name="new_entry"),
    path("random/", views.random_page, name='random'),
    path("edit_entry/<str:title>", views.edit_entry, name="edit_entry"),
]
