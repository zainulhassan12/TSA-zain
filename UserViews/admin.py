from django.contrib import admin

from .models import *



# admin.site.register(UserApplication)
admin.site.register(Application)
admin.site.register(grades)
admin.site.register(canAccess)


