from django.contrib import admin
from .models import Users

class UserAdmin(admin.ModelAdmin):
    list = ('name')

admin.site.register(Users, UserAdmin)

