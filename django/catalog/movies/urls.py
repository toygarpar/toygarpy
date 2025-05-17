from django.urls import path
from . import views


#127.0.0.1:8000/movies
#127.0.0.1:8000/movies/2 ------>      int:movie_id
#127.0.0.1:8000/movies/search

urlpatterns = [
    path("", views.index, name="movies"),
    path("<int:movie_id>", views.details, name="details"),
    path("search", views.search, name="search"),


]