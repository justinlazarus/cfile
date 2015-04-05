from django.db import models

class Entry(models.Model):
	date = models.DateTimeField()
	title = models.SlugField()
	description = models.TextField()
	image = models.ImageField()

