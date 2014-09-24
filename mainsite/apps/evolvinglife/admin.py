from django.contrib import admin
import models

class UserPointInLine(admin.TabularInline):
	model = models.UserPoint

class GeographyPointInLine(admin.TabularInline):
	model = models.GeographyPoint

class UserAdmin(admin.ModelAdmin):
	list_display = ('ip', 'symbol', 'colour', 'time')
	inlines = [UserPointInLine]

class GeographyAdmin(admin.ModelAdmin):
	list_display = ('category', 'symbol', 'colour')
	inlines = [GeographyPointInLine]

# Register your models here.
admin.site.register(models.User, UserAdmin)

admin.site.register(models.Geography, GeographyAdmin)
