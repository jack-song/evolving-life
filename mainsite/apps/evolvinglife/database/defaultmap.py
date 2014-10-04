from mainsite.apps.evolvinglife import models

landgeography = models.Geography.objects.get(category = "land")

for x in range(0, 50):
	for y in range (0, 50):
		newpoint = models.GeographyPoint(x = x, y = y, geography = landgeography)
		newpoint.save()