from django.urls import path
from . import views
from . import apps

app_name = apps.ApisConfig.name

urlpatterns = [
    path('upload', views.upload, name="upload"),
    path('create', views.create, name="create"),
    path('create/success', views.success, name="success"),
    path('scrapper', views.scrapper, name="scrapper"),
    path('books', views.ListBooks.as_view(), name="books")
]
