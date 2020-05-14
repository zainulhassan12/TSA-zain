from django.urls import path
from . import views

app_name = 'InterviewPannel'
urlpatterns = [
    path('', views.interhome, name='interhome'),
    path('quiz/', views.QuizView, name='quiz'),
    path('question/', views.QuestionAdd, name='question'),
    path('question1/', views.ans, name='question1')
]
