from django.contrib import admin

from .models import Representative

class RepresentativeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'type', 'status')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('type', 'status')


admin.site.register(Representative, RepresentativeAdmin)
