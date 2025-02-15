from django.db import models

# Create your models here.
class Restaurant(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True)
	opening_time = models.TimeField()
	closing_time = models.TimeField()
	
	def __str__(self):
		return self.name

