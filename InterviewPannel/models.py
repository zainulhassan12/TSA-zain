from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify


class Quiz(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(verbose_name="Description", null=True, )
    # Count = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp', ]
        verbose_name_plural = "Quizzes"

    def __str__(self):
        return self.name


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
    instance.slug = slugify(instance.name)
