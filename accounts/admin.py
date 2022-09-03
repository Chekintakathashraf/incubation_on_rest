from django.contrib import admin

from accounts.models import CustomUser,Application, Slots

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Application)
admin.site.register(Slots)