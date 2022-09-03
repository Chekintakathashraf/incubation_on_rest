from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import CustomUser,Application, Slots

class CustomUserAdmin(UserAdmin):
    list_display=('id','name','email','username')

class ApplicationAdmin(admin.ModelAdmin):
    list_display=('id','username','company_name','status')

class SlotAdmin(admin.ModelAdmin):
    list_display=('id','serial_number','company_name')
# Register your models here.
admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Application,ApplicationAdmin)
admin.site.register(Slots,SlotAdmin)