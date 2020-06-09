from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple

from .models import *


class QuizForm(forms.ModelForm):
    description = forms.CharField(help_text="Add Description for this Quiz", widget=forms.Textarea(
        attrs={
            'rows': 4,
            'cols': 2
        }

    )
                                  )

    success_text = forms.CharField(help_text=" Text to display on successful attempt of quiz", widget=forms.Textarea(
        attrs={
            'rows': 4,
            'cols': 2
        }

    )
                                   )
    explanation = forms.CharField(help_text="Explanation to be shown "
                                            "after the question has "
                                            "been answered.", widget=forms.Textarea(
        attrs={
            'rows': 4,
            'cols': 2
        }
    )
                                  )
    fail_text = forms.CharField(help_text="Text to display on faliure", widget=forms.Textarea(attrs={
        'rows': 4,
        'cols': 2
    }
    )
                                )

    # answers_at_end = forms.BooleanField(help_text="if this is checked answers will be shown at end", initial=False,
    #                                     label="Answer at end")

    class Meta:
        model = Quiz
        fields = [
            'title', 'description', 'explanation', 'category', 'answers_at_end', 'single_attempt', 'success_text',
            'fail_text'

        ]


class questions(forms.ModelForm):
    class Meta:
        model = Questions
        fields = [
            'question',
        ]


class answers(forms.ModelForm):
    class Meta:
        model = Answers
        fields = [
            'question', 'answer', 'is_correct',
        ]


class Add_Questions_to_Quiz(forms.ModelForm):
    queryset = Questions.objects.all()
    question = forms.ModelMultipleChoiceField(label="Select Available Questions",
                                              help_text="Select Question To Add In Quiz!!",
                                              widget=FilteredSelectMultiple('Questions', is_stacked=False),
                                              queryset=queryset)

    class Media:
        css = {'all': ('/static/admin/css/widgets.css', '/static/admin/css/overrides.css'), }
        js = ('/admin/jsi18n',)

    class Meta:
        model = QuizQuestion
        fields = [
            'quiz', 'question'
        ]
