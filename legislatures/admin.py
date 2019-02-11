from django.contrib import admin

from .models import Legislature
from .models import ParliamentaryGroup

class LegislatureAdmin(admin.ModelAdmin):
    list_display = (
        '__str__', 'system', 'year', 'start_data', 'percentage'
    )

class ParliamentaryGroupAdmin(admin.ModelAdmin):
    list_display = (
        '__str__', 'group', 'percentage_women'
    )

admin.site.register(Legislature, LegislatureAdmin)
admin.site.register(ParliamentaryGroup, ParliamentaryGroupAdmin)
