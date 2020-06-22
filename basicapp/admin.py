from django.contrib import admin
from basicapp.models import Traffic


class TrafficAdmin(admin.ModelAdmin):
	list_display = ["ip", "created"]


admin.site.register(Traffic, TrafficAdmin)

