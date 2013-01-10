from django.db import models
from movies.models import Movie

# Comment model
class Comment(models.Model):
	author = models.CharField(max_length=100)
	mail = models.EmailField()
	url = models.URLField()
	message = models.TextField()
	movie = models.ForeignKey(Movie)

	def __unicode__(self):
		return "%s %s" % (self.author, self.message)
