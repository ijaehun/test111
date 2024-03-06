from django.contrib import admin

# Register your models here.

from .models import User

class userAdmin(admin.ModelAdmin):
    list_display = ('Username', 'password')

admin.site.register(User, userAdmin)