from django.contrib import admin

from .models import Legislature

class LegislatureAdmin(admin.ModelAdmin):
    list_display = (
        '__str__', 'system', 'year', 'start_data', 'percentage'
    )

admin.site.register(Legislature, LegislatureAdmin)
