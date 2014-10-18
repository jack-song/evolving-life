# coding: utf-8
from models import Geography
from models import GeographyPoint
from django.shortcuts import render
from django.core import serializers

def index(request):
	#use natural key to serialize needed fields from geographys easily
	#from each geography point
	geographypoints_json = serializers.serialize("json", GeographyPoint.objects.all(), use_natural_keys=True)

	context = {
		"geographypoints": geographypoints_json
	}

	return render(request, "index.html", context)