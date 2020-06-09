from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple

from .models import Questions, Quiz, Answers, Category, QuizQuestion


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('category',)


class QuizAdminForm(forms.ModelForm):

    list_display = ('title', 'category',)
    list_filter = ('category',)
    search_fields = ('description', 'category',)

    class Meta:
        model = Quiz
        exclude = []

    questions = forms.ModelMultipleChoiceField(
        queryset=Questions.objects.filter(),
        required=False,
        label="Questions")
        # widget=FilteredSelectMultiple(
        #     verbose_name="Questions",
        #     is_stacked=False))

    # def __init__(self, *args, **kwargs):
    #     super(QuizAdminForm, self).__init__(*args, **kwargs)
    #     if self.instance.id:
    #         self.fields['questions'].initial = \
    #             self.instance.question_set.all()

    # def save(self, commit=True):
    #     quiz = super(QuizAdminForm, self).save(commit=False)
    #     quiz.save()
    #     quiz.question_set.set(self.cleaned_data['question'])
    #     self.save_m2m()
    #     return quiz


class QuizAdmin(admin.ModelAdmin):
    form = QuizAdminForm
    list_display = ('title', 'category',)
    list_filter = ('category',)
    search_fields = ('description', 'category',)


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Questions)
admin.site.register(Answers)
admin.site.register(QuizQuestion)
