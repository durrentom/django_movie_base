# Create your views here.
from movies.models import *
from django.shortcuts import render

def home(request):
	foo = "Hello Foo"
	return render(request,'movies/home.html', {'foo': foo})

def now(request):
	import datetime
	now = datetime.datetime.now()
	return render(request,'movies/home.html', {'foo': now.strftime("%Y-%m-%d %H:%M:%S")})

def movies(request):
	movies = Movie.objects.all()
	return render(request,'movies/movies.html', {'movies': movies})

def movie_details(request, slug):
	movie = Movie.objects.get(slug=slug)
	return render(request,'movies/movie_details.html', {'movie': movie})

def director_details(request, slug):
	director = Director.objects.get(slug=slug)
	return render(request,'director/director_details.html', {'director': director})