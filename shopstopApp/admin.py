from django.contrib import admin
from shopstopApp.models import Setting

# Register your models here.
class SettingAdmin(admin.ModelAdmin):
    list_display = ['title','company', 'updated_at','status']
    
    
admin.site.register(Setting,SettingAdmin)