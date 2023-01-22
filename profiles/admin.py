from django.contrib import admin
from . models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """ Profile admin registration """
    list_display = ('id', 'user', 'first_name')
