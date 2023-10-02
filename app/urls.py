from django.urls import path
from app import views

urlpatterns = [
    path("quiz_movie/", views.IndexView.as_view(), name="index"),
]
