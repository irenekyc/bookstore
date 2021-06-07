from django.urls import path
from . import apps
from . import views

app_name = apps.BooksConfig.name

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("category", views.category, name="category"),
    path("category/<str:category_name>", views.category_list, name="category_list"),
    path("books/<str:book_slug>", views.book_details, name="book_details")

]
