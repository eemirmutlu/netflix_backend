from django.contrib import admin
from .models import *


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')


admin.site.register(Profile, ProfileAdmin)
# Register your models here.
