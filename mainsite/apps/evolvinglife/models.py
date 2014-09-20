from django.db import models
from libs.fields import ColourField

# Create your models here.
class User(models.Model):
	ip = models.GenericIPAddressField(unique=True)
	colour = ColourField(unique=True)
	symbol = models.CharField(max_length=1, unique=True)
	time = models.DateTimeField(auto_now_add=True)

class UserPoint(models.Model):
	x = models.IntegerField()
	y = models.IntegerField()
	user = models.ForeignKey(User)

class Geography(models.Model):
	category = models.TextField(unique=True)
	colour = ColourField(unique=True)
	symbol = models.CharField(max_length=1, unique=True)

class GeographyPoint(models.Model):
	x = models.IntegerField()
	y = models.IntegerField()
	geography = models.ForeignKey(Geography)