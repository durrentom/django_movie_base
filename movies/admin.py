from django.contrib import admin
from movies.models import Director, Movie, Country

#Director
class DirectorAdmin(admin.ModelAdmin):
	model = Director

admin.site.register(Director, DirectorAdmin)

#Movie
class MovieAdmin(admin.ModelAdmin):
	model = Movie
	list_display = ('title', 'year', 'director', 'country')

admin.site.register(Movie, MovieAdmin)

#Country
class CountryAdmin(admin.ModelAdmin):
	model = Country

admin.site.register(Country, CountryAdmin)