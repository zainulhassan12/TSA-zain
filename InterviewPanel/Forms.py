from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple

from .models import *


class QuizForm(forms.ModelForm):
    description = forms.CharField(help_text="Add Description for this Quiz", widget=forms.Textarea(
        attrs={
            'rows': 4,
            'cols': 2
        }))
    Instructions = forms.CharField(help_text="Add Instructions for this Quiz", widget=forms.Textarea(
        attrs={
            'rows': 4,
            'cols': 2
        }))

    success_text = forms.CharField(help_text=" Text to display on successful attempt of quiz", widget=forms.Textarea(
        attrs={'rows': 4, 'cols': 2}))
    # explanation = forms.CharField(help_text="Explanation to be shown "
    #                                         "after the question has "
    #                                         "been answered.", widget=forms.Textarea(
    #     attrs={
    #         'rows': 4,
    #         'cols': 2
    #     }
    # )
    # )
    fail_text = forms.CharField(help_text="Text to display on faliure", widget=forms.Textarea(attrs={
        'rows': 4,
        'cols': 2
    }
    )
                                )

    # answers_at_end = forms.BooleanField(help_text="if this is checked answers will be shown at end", initial=False,
    #                                     label="Answer at end")
    queryset = Questions.objects.all()
    questions = forms.ModelMultipleChoiceField(label="Select Available Questions",
                                               help_text="Select Question To Add In Quiz!!",
                                               widget=FilteredSelectMultiple('Questions', is_stacked=False),
                                               queryset=queryset)

    class Media:
        css = {'all': ('/static/admin/css/widgets.css', '/static/admin/css/overrides.css', 'admin/css/base.css',
                       'admin/css/responsive.css'), }
        js = ('/admin/jsi18n',)

    class Meta:
        model = Quiz
        fields = [
            'title', 'description', 'Instructions', 'url', 'category', 'answers_at_end', 'single_attempt',
            'success_text',
            'fail_text'

        ]

    def __init__(self, *args, **kwargs):
        super(QuizForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['questions'].initial = \
                self.instance.questions_set.all().select_subclasses()

    def save(self, commit=True):
        quiz = super(QuizForm, self).save(commit=False)
        quiz.url = slugify(quiz.title)
        quiz.save()
        quiz.questions_set.set(self.cleaned_data['questions'])
        self.save_m2m()
        return quiz


class AddingNewQuestions(forms.Form):
    # quiz = forms.ModelChoiceField(widget=forms.RadioSelect(attrs=
    #                                                        {
    #                                                            'class': 'form-check'
    #                                                        }),
    #                               queryset=Quiz.objects.all(),
    #                               label="Quizzes",
    #                               help_text="Select a Quiz to which this Question Belong")

    explanation = forms.CharField(help_text="Explanation At End",
                                  widget=forms.Textarea(
                                      attrs={
                                          'rows': 4,
                                          'cols': 50
                                      }
                                  ))
    question = forms.CharField(help_text="Add Your Question,Limit Is 1000 words", widget=forms.TextInput())

    class Media:
        css = {'all': ('admin/css/base.css', 'admin/css/responsive.css'), }

    class Meta:
        model = Questions
        fields = [
            'quiz', 'question', 'explanation'
        ]


class InterviewForm(forms.ModelForm):
    Personality = forms.IntegerField(max_value=10, min_value=0, widget=forms.NumberInput(),
                                     help_text="Personality Marks__Range(1,10)",
                                     label="Personality Marks")
    Dressing_Sense = forms.IntegerField(max_value=10, min_value=0, help_text="Dressing Sense Marks __Range(1,10",
                                        widget=forms.NumberInput())
    Communication_Skills = forms.IntegerField(max_value=10, min_value=0,
                                              help_text="Communication Skills Marks__Range(1,10)",
                                              widget=forms.NumberInput())
    InterView_Questions = forms.IntegerField(max_value=10, min_value=0,
                                             help_text="InterVew Questions  Marks__Range(1,10)",
                                             widget=forms.NumberInput())
    total_marks_for_interview = forms.FloatField(required=False)

    class Meta:
        model = InterviewModel
        fields = [
            'user', 'Personality', 'Dressing_Sense', 'Communication_Skills', 'InterView_Questions',
            'total_marks_for_interview'
        ]


class InterQuestion(forms.ModelForm):
    Question = forms.CharField(widget=forms.TextInput(), help_text="Question To Ask in Interview", )
    Explanation = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, }),
                                  help_text="Explanation For Question")

    class Meta:
        model = InterviewQuestions
        fields = [
            'Question', 'Explanation',
        ]


class CSVUploadForm(forms.ModelForm):
    # file = forms.FileField(help_text="Upload Csv File", required=False)

    class Meta:
        model = CSVUpload
        fields = [
            'title', 'file', 'Uploaded_by'
        ]

    # def clean_file(self, *args, **kwargs):
    #     file = self.cleaned_data.get("file")
    #     if not file.endswith(".csv"):
    #         raise forms.ValidationError("This is not a Valid File.Must use '.csv'")
    #     return file

# class Add_Questions_to_Quiz(forms.ModelForm):
#     queryset = Questions.objects.all()
#     question = forms.ModelMultipleChoiceField(label="Select Available Questions",
#                                               help_text="Select Question To Add In Quiz!!",
#                                               widget=FilteredSelectMultiple('Questions', is_stacked=False),
#                                               queryset=queryset)
#
#     class Media:
#         css = {'all': ('/static/admin/css/widgets.css', '/static/admin/css/overrides.css', 'admin/css/base.css',
#                        'admin/css/responsive.css'), }
#         js = ('/admin/jsi18n',)
#
#     class Meta:
#         model = QuizQuestion
#         fields = [
#             'quiz', 'question'
#         ]

#
# class answers(forms.ModelForm):
#     class Meta:
#         model = Answers
#         fields = [
#             'question', 'answer', 'is_correct',
#         ]

# class Quiz(forms.Form):
#     Questions =
