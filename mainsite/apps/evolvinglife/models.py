from django.db import models

# Create your models here.
class User(models.Model):
	ip = models.GenericIPAddressField(unique=True)
	colour = models.IntegerField(unique=True)
	symbol = models.CharField(max_length=1, unique=True)
	time = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.ip

class UserPoint(models.Model):
	x = models.IntegerField()
	y = models.IntegerField()
	user = models.ForeignKey(User)

	def __unicode__(self):
		return str(self.x) + "," + str(self.y) + " : " + "\"" + self.user.symbol + "\""

class Geography(models.Model):
	category = models.TextField(unique=True)
	colour = models.IntegerField(unique=True)
	symbol = models.CharField(max_length=1, unique=True)

	def natural_key(self):
		return (self.colour, self.symbol)

	def __unicode__(self):
		return self.category

class GeographyPoint(models.Model):
	x = models.IntegerField()
	y = models.IntegerField()
	geography = models.ForeignKey(Geography)

	def __unicode__(self):
		return str(self.x) + "," + str(self.y) + " : " + "\"" + self.geography.symbol + "\""