from django import forms

from .models import *


# from formfieldset.forms import FieldsetMixin

class testform(forms.ModelForm):
    class Meta:
        model = test1
        fields = [
            'name', 'address',
        ]


class applicationForm(forms.ModelForm):
    class Meta:
        model = UserApplication
        fields = [
            'First_Name', 'Last_Name', 'First_NameF', 'Last_NameF', 'Age', 'Date_of_Birth', 'Gender', 'Experience',
            'Qualify', 'Image',
        ]


class Uapplication(forms.ModelForm):
    First_Name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Name',
        'label': 'Name'
    }))
    Last_Name = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Last Name'
        }
    ))
    Father_Name = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Full Name'
        }
    ))
    Email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'placeholder': 'abc@xyz.com'
        }))
    MatricTotal = widgets = forms.NumberInput(attrs={
        'min': 0,
        'range': 0 - 1100,
    })
    IntermediateTotal = forms.IntegerField(initial=0, max_value=1100)
    Date_of_Birth = forms.DateField(
        widget=forms.SelectDateWidget(attrs={'placeholder': 'Date'},
                                      empty_label=("Choose Year", "Choose Month", "Choose Day"),
                                      years=range(1970, 2020)
                                      )
    )

    class Meta:
        model = Application
        fields = [
            'First_Name', 'Last_Name', 'Father_Name', 'Domicile', 'Age', 'Date_of_Birth', 'Gender', 'Phone_no',
            'Land_Line', 'Email',
            'MatricTotal', 'MatricObtain', 'MatricSubject', 'MatricPercentage', 'MatricGrades', 'MatricYear',
            'IntermediateTotal', 'IntermediateObtain', 'IntermediateSubject', 'IntermediatePercentage',
            'IntermediateGrades', 'IntermediateYear',
            'GraduationTotal', 'GraduationObtain', 'GraduationSubject', 'GraduationPercentage', 'GraduationGrades',
            'GraduationYear',
            'Matrics_Result', 'Graduations_result', 'Intermediate_result', 'Image', 'Qualify', 'Speclization',
            'Experience',
            'Master_Specialization',
        ]
        # fieldsets = (
    #     (u'Primary Information', {
    #         'fields': ['First_Name', 'Last_Name', 'Father_Name', 'Domicile', 'Age', 'Date_of_Birth', 'Gender',
    #                    ' Phone_no', 'Land_Line']}),
    #     (u'Study Information', {
    #         'fields': [' Matric', ' Intermediate', ' Graduation', ' Total', ' Obtain ', 'Subject',
    #                    ' Percentage', ' Grades', ' Year', ' Matric_Result', ' Graduation_result', '  Image']}),
    #     (u'Matric', {'fields': [' Total', ' Obtain ', '  Subject', ' Percentage', ' Grades', ' Year']}),
    #     (u'Intermediate', {'fields': [' Total', ' Obtain ', '  Subject', ' Percentage', ' Grades', ' Year']}),
    #     (u'Graduation', {'fields': [' Total', ' Obtain ', '  Subject', ' Percentage', ' Grades', ' Year']}),
    #     (u'Short Information', {
    #         'fields': [' Graduations_result', '  Image', '  Qualify', ' Speclization', 'Experience',
    #                    'Master_Specialization']}),
    # )

    # class MyForm(Form, FieldsetMixin):
    #     fieldsets = (
    #         (u'Primary Information', {
    #             'fields': ['First_Name', 'Last_Name', 'Father_Name', 'Domicile', 'Age', 'Date_of_Birth', 'Gender',
    #                        ' Phone_no', 'Land_Line']}),
    #         (u'Study Information', {
    #             'fields': [' Matric', ' Intermediate', ' Graduation', ' Total', ' Obtain ', 'Subject',
    #                        ' Percentage', ' Grades', ' Year', ' Matric_Result', ' Graduation_result', '  Image']}),
    #         (u'Matric', {'fields': [' Total', ' Obtain ', '  Subject', ' Percentage', ' Grades', ' Year']}),
    #         (u'Intermediate', {'fields': [' Total', ' Obtain ', '  Subject', ' Percentage', ' Grades', ' Year']}),
    #         (u'Graduation', {'fields': [' Total', ' Obtain ', '  Subject', ' Percentage', ' Grades', ' Year']}),
    #         (u'Short Information', {
    #             'fields': [' Graduations_result', '  Image', '  Qualify', ' Speclization', 'Experience',
    #                        'Master_Specialization']}),
    #     )


class test(forms.Form):
    First_Name = forms.CharField(max_length=50, required=True)
    Last_Name = forms.CharField(max_length=50, required=True)
