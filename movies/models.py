from django.db import models

class Director(models.Model):
	slug = models.SlugField(max_length=200)
	name = models.CharField(max_length=200)
	forename = models.CharField(max_length=200)
	
	def __unicode__(self):
		return "%s %s" % (self.forename, self.name)

class Country(models.Model):
	slug = models.SlugField(max_length=200)
	name = models.CharField(max_length=200)

	def __unicode__(self):
		return "%s" % (self.name)

class Movie(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200)
	picture = models.FileField(upload_to='movies/pictures')
	year = models.DateField()
	synopsis = models.TextField()

	director = models.ForeignKey('Director')
	country = models.ForeignKey('Country')

	def __unicode__(self):
		return "%s %s" % (self.title, self.year)