import re

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify


class CategoryManager(models.Manager):

    def new_category(self, category):
        new_category = self.create(category=re.sub('\s+', '-', category)
                                   .lower())

        new_category.save()
        return new_category


class Category(models.Model):
    category = models.CharField(
        verbose_name="Category",
        max_length=250, blank=True,
        unique=True, null=True)

    objects = CategoryManager()

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category


class Quiz(models.Model):
    title = models.CharField(
        verbose_name="Title",
        max_length=60, blank=False,
        help_text=" Descriptive Title For Quiz"
    )
    description = models.TextField(verbose_name="Description", null=True,
                                   help_text="Add some meaningful information about this Quiz.")
    explanation = models.TextField(max_length=2000,
                                   blank=True,
                                   help_text=("Explanation to be shown "
                                              "after the question has "
                                              "been answered."),
                                   verbose_name=('Explanation'))
    # Count = models.IntegerField()
    category = models.ForeignKey(
        Category, null=True, blank=True,
        verbose_name="Category", on_delete=models.CASCADE,help_text="To Manage The Quizzes Assign a Categeory")

    answers_at_end = models.BooleanField(
        blank=False, default=False,
        help_text=("Correct answer is NOT shown after question."
                   " Answers displayed at the end."),
        verbose_name="Answers at end")

    single_attempt = models.BooleanField(
        blank=False, default=False,
        help_text=("If yes, only one attempt by"
                   " a user will be permitted."
                   " Non users cannot sit this exam."),
        verbose_name="Single Attempt")
    success_text = models.TextField(
        blank=True, help_text="Displayed if user passes.",
        verbose_name="Success Text")

    fail_text = models.TextField(
        verbose_name="Fail Text",
        blank=True, help_text="Displayed if user fails.")

    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp', ]
        verbose_name = "Quiz"
        verbose_name_plural = "Quizzes"

    def __str__(self):
        return self.title

    def get_questions(self):
        return self.question_set.all().select_subclasses()

    @property
    def get_max_score(self):
        return self.get_questions().count()


class Questions(models.Model):
    quiz = models.ManyToManyField(Quiz, verbose_name='Quiz', null=True)
    question = models.CharField(max_length=2000)

    def __str__(self):
        return self.question


class Answers(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, null=True)
    answer = models.CharField(max_length=500)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer


class QuizQuestion(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)


# class join(models.Model):
#     quiz = models.ForeignKey()
#     question = models.ForeignKey(Quiz, on_delete=models.CASCADE


# class correct(models.Model):
#     question = models.ForeignKey(Questions, on_delete=models.CASCADE)
#     is_correct = models.BooleanField(default=False)


# class QuizTaker(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
#     score = models.IntegerField(default=0)
#     completed = models.BooleanField(default=False)
#     date_finished = models.DateTimeField(null=True)
#     timestamp = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.user.email
#

@receiver(pre_save, sender=Quiz)
def slugify_name(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.title)
