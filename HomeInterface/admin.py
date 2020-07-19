from django.contrib import admin

from .models import *

admin.site.site_header = 'Teacher Selection Assistance'
admin.site.site_title = 'TSA'
admin.site.name = 'Teacher Selection Assistance'


class UserInterace(admin.ModelAdmin):
    list_display = ('location', 'Age',)
    list_filter = ('location', 'Age')
    change_list_template = 'admin/teacher_change_list.html'


admin.site.register(User_profile, UserInterace)
