from django.contrib import admin
from . import models

# Register your models here.
class fooditemAdmin(admin.ModelAdmin):
    list_display = ["name", "type", "VitaminPresent"]
    list_filter = ["type"]
    search_fields = ["name"]
    # alphabetical_list_filter = ["name"]


admin.site.register(models.fooditem, fooditemAdmin)
