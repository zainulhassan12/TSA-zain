from django.urls import path

from . import views

app_name = 'InterviewPannel'
urlpatterns = [
    path('', views.interhome, name='interhome'),
    path('Quiz/', views.QuizView, name='quiz'),
    path('question/', views.QuestionAdd, name='question'),
    path('AddQuestion/', views.ans, name='question1'),
    path('Questions/', views.Questions_Detail_view, name="viewQuestions")
]
