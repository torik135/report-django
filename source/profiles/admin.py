from django.contrib import admin
from .models import Profiles

class ProfilesAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar', 'created', 'updated')

admin.site.register(Profiles, ProfilesAdmin)