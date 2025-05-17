from django.shortcuts import render

from django.shortcuts import get_object_or_404

from .models import Movie

from django.http import Http404



# Create your views here.



def index(request):
    movies = Movie.objects.all


    context = {
        "movies" : movies
    }


    return render(request, "movies/list.html", context)


def details(request, movie_id):
    # try:
    #     movie = Movie.objects.get(pk = movie_id)
    # except Movie.DoesNotExist:
    #     raise Http404("The Movie you have been searching for does not exist!")
    # try except ile uğraşmamak için method import yukarda

    movie = get_object_or_404(Movie, pk = movie_id)

    context = {
        "movie": movie
    }



    return render(request, "movies/details.html", context)


def search(request):
    return render(request, "movies/search.html")
