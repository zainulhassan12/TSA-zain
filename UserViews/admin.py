from django import forms
from django.contrib import admin

from .UserViewsForms import UserGrades
from .models import *


class ApplicantGradeForm(admin.ModelAdmin):
    form = UserGrades
    list_display = ('user', 'Speciality',)
    search_fields = ('user',)


class ApplicationAdmin(admin.ModelAdmin):
    model = Application
    list_display = ('First_Name', 'Last_Name', 'Email')
    list_filter = ('First_Name', 'Domicile', 'Age')


class GradesAdmin(admin.ModelAdmin):
    model = grades
    list_display = ('user', 'category', 'quiz', 'total_marks','obtained_marks','percentage','timestamp')
    list_filter = ('user', 'category')


class AccessForm(forms.ModelForm):
    QuizName = forms.ModelChoiceField(queryset=Quiz.objects.all())

    class Meta:
        model = canAccess
        fields = ['user', 'QuizName']


class accessadmin(admin.ModelAdmin):
    form = AccessForm
    model = canAccess
    list_display = ('user', 'QuizName',)


admin.site.register(ApplicantGradesInformation, ApplicantGradeForm)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(grades, GradesAdmin)
admin.site.register(canAccess, accessadmin)
