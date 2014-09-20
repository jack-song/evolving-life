from django.db import models

# Create your models here.
class User(models.Model):
	ip = models.GenericIPAddressField(unique=True)
	colour = models.IntegerField(unique=True)
	symbol = models.CharField(max_length=1, unique=True)
	time = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.symbol

class UserPoint(models.Model):
	x = models.IntegerField()
	y = models.IntegerField()
	user = models.ForeignKey(User)

	def __unicode__(self):
		return self.x + "," + self.y + " : " + self.symbol

class Geography(models.Model):
	category = models.TextField(unique=True)
	colour = models.IntegerField(unique=True)
	symbol = models.CharField(max_length=1, unique=True)

	def __unicode__(self):
		return self.symbol

class GeographyPoint(models.Model):
	x = models.IntegerField()
	y = models.IntegerField()
	geography = models.ForeignKey(Geography)

	def __unicode__(self):
		return self.x + "," + self.y + " : " + self.symbol