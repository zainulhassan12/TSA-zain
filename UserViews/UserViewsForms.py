from django import forms
from django.forms import RadioSelect

from InterviewPanel.models import Answers
from .models import *

# from formfieldset.forms import FieldsetMixin
GRADES_CHOICES = [
    ('1', 'A+'),
    ('2', 'A'),
    ('3', 'B+'),
    ('4', 'B'),
    ('5', 'B-'),
    ('6', 'C+'),
    ('7', 'C'),
    ('8', 'D'),
]


class questions(forms.Form):
    question = forms.CharField()
    answers = forms.ChoiceField(choices=[],
                                widget=RadioSelect())

    def __init__(self, question, *args, **kwargs):
        super(questions, self).__init__(*args, **kwargs)
        self.fields["question"].queryset = question
        self.fields["answers"].choices = self.get_answers_list(question)

    def get_answers_list(self, question):
        return [(answer.id, answer) for answer in Answers.objects.filter(question__in=question)]


class testform(forms.ModelForm):
    class Meta:
        model = test1
        fields = [
            'name', 'address',
        ]


# class applicationForm(forms.ModelForm):
#     class Meta:
#         model = UserApplication
#         fields = [
#             'First_Name', 'Last_Name', 'First_NameF', 'Last_NameF', 'Age', 'Date_of_Birth', 'Gender', 'Experience',
#             'Qualify', 'Image',
#         ]


class Uapplication(forms.ModelForm):
    First_Name = forms.CharField(help_text="Your Names First word e.g 'Zain' for 'Zain ul hassan'",
                                 widget=forms.TextInput(attrs={
                                     'placeholder': 'Your Name',
                                     'label': 'Name'
                                 }))
    Last_Name = forms.CharField(help_text="Your Names Last word e.g 'ul hassan' for 'Zain ul hassan'",
                                widget=forms.TextInput(
                                    attrs={
                                        'placeholder': 'Last Name'
                                    }
                                ))
    Father_Name = forms.CharField(help_text="Your Fathers Full Name e.g 'Ansar Mehmood'", widget=forms.TextInput(
        attrs={
            'placeholder': 'Full Name'
        }
    ))
    Email = forms.EmailField(
        help_text="Your Valid Email Address As this is used to reset your password if u forgot.Also for the "
                  "Important notifications by Administration ",
        widget=forms.TextInput(
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


class UserGrades(forms.Form):
    speciality = forms.CharField(max_length=1000, help_text="You have entered in the Application..Now Enter Grades",
                                 disabled=True)
    NetworkSecurity = forms.ChoiceField(choices=GRADES_CHOICES, label="NS",
                                        widget=forms.RadioSelect(attrs={}))
    DataCommunicationAndComputerNetworks = forms.ChoiceField(choices=GRADES_CHOICES, label="DCN",
                                                             widget=forms.RadioSelect(attrs={}), )

    WirelessAndMobileCommunication = forms.ChoiceField(choices=GRADES_CHOICES, label="WMC",
                                                       widget=forms.RadioSelect(attrs={}))
    InternetArchitectureAndProtocol = forms.ChoiceField(choices=GRADES_CHOICES, label="IAP",
                                                        widget=forms.RadioSelect(attrs={}))
    ProgrammingFundamentals = forms.ChoiceField(choices=GRADES_CHOICES, label="PF",
                                                widget=forms.RadioSelect(attrs={}))
    ObjectOrientedProgramming = forms.ChoiceField(choices=GRADES_CHOICES, label="OOP",
                                                  widget=forms.RadioSelect(attrs={}))
    DataStructuresAndAlgorithms = forms.ChoiceField(choices=GRADES_CHOICES, label="DSA",
                                                    widget=forms.RadioSelect(attrs={}))
    VisualProgramming = forms.ChoiceField(choices=GRADES_CHOICES, label="VP",
                                          widget=forms.RadioSelect(attrs={}))
    WebSystemAndTechnologies = forms.ChoiceField(choices=GRADES_CHOICES, label="WST",
                                                 widget=forms.RadioSelect(attrs={}))
    MobileApplicationDevelopment = forms.ChoiceField(choices=GRADES_CHOICES, label="MAD",
                                                     widget=forms.RadioSelect(attrs={}))
    CloudComputing = forms.ChoiceField(choices=GRADES_CHOICES, label="CC",
                                       widget=forms.RadioSelect(attrs={}))
    ArtificialIntelligence = forms.ChoiceField(choices=GRADES_CHOICES, label="AI",
                                               widget=forms.RadioSelect(attrs={}))
    DataMining = forms.ChoiceField(choices=GRADES_CHOICES, label="DM",
                                   widget=forms.RadioSelect(attrs={}))
    CalculusAndAnalyticalGeometry = forms.ChoiceField(choices=GRADES_CHOICES, label="Calculus",
                                                      widget=forms.RadioSelect(attrs={}))
    LinearAlgebra = forms.ChoiceField(choices=GRADES_CHOICES, label="LA",
                                      widget=forms.RadioSelect(attrs={}))
    DiscreteStructures = forms.ChoiceField(choices=GRADES_CHOICES, label="Discrete",
                                           widget=forms.RadioSelect(attrs={}))
