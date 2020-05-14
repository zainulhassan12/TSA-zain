from django.contrib import admin
from django.contrib.auth.models import User

from .models import *

admin.site.site_header = 'Teacher Selection Assistance'
admin.site.site_title = 'TSA'


class UserInterace(admin.ModelAdmin):
    list_display = ('location', 'Age',)
    list_filter = ('location', 'Age')
    change_list_template = 'admin/teacher_change_list.html'


admin.site.register(User_profile, UserInterace)
