from django.urls import path
from django.conf.urls import url
from django import views as django_views
from django.views.i18n import JavaScriptCatalog

from . import views

app_name = 'InterviewPanel'
urlpatterns = [
    url(r'^jsi18n/$', django_views.i18n.JavaScriptCatalog.as_view(), name='jsi18n'),
    path('', views.interhome, name='interhome'),
    path('Quiz/', views.QuizView, name='quiz'),
    path('question/', views.QuestionAdd, name='question'),
    path('AddQuestion/', views.ans, name='question1'),
    path('Questions/', views.Questions_Detail_view, name="viewQuestions"),
    path('FinalQuiz/', views.Add_Questions, name="AddQuestionToQuiz"),
    path('CheckingQuizDetails', views.GetQuizData, name="DetailOfQuiz"),


]
