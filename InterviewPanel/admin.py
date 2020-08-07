from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.utils.translation import ugettext_lazy as _

from .models import Questions, Quiz, Category, Answers, InterviewModel, InterviewQuestions


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('category',)


class QuizAdminForm(forms.ModelForm):
    """
        below is from
        http://stackoverflow.com/questions/11657682/
        django-admin-interface-using-horizontal-filter-with-
        inline-manytomany-field
    """

    class Meta:
        model = Quiz
        exclude = []

    questions = forms.ModelMultipleChoiceField(
        queryset=Questions.objects.all(),
        required=False,
        label=_("Questions"),
        widget=FilteredSelectMultiple(
            verbose_name=_("Questions"),
            is_stacked=False))

    def __init__(self, *args, **kwargs):
        super(QuizAdminForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['questions'].initial = \
                self.instance.questions_set.all()

    def save(self, commit=True):
        quiz = super(QuizAdminForm, self).save(commit=False)
        quiz.save()
        quiz.questions_set.set(self.cleaned_data['questions'])
        self.save_m2m()
        return quiz


class QuizAdmin(admin.ModelAdmin):
    form = QuizAdminForm
    list_display = ('title', 'category',)
    list_filter = ('category',)
    search_fields = ('description', 'category',)


class AnswerInline(admin.TabularInline):
    search_fields = ('answer',)
    model = Answers


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question',)
    list_filter = ('question',)
    search_fields = ('question',)
    inlines = [
        AnswerInline,
    ]


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Questions, QuestionAdmin)
admin.site.register(InterviewModel)
admin.site.register(InterviewQuestions)
