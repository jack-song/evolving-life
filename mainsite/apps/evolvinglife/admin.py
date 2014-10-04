from django.contrib import admin
import models

class UserPointInLine(admin.TabularInline):
	model = models.UserPoint

# may be too many to display at some point, but currently at 50 * 50
# should be ok
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
