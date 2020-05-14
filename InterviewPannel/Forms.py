from django import forms

from .models import *


class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = [
            'name', 'description',

        ]


class questions(forms.ModelForm):
    class Meta:
        model = Questions
        fields = [
            'quiz', 'question'
        ]


class answers(forms.ModelForm):
    class Meta:
        model = Answers
        fields = [
            'question', 'answer', 'is_correct',
        ]
