from django.contrib import admin
from .models import Bcuser

# Register your models here.

class BcuserAdmin(admin.ModelAdmin):
    list_display=('username','password')
admin.site.register(Bcuser, BcuserAdmin)

# 병준 admin