from django import views as django_views
from django.conf.urls import url
from django.urls import path, re_path
from django.views.i18n import JavaScriptCatalog

from . import views
from .views import QuizListView, QuizDetailView

app_name = 'InterviewPanel'
urlpatterns = [
    url(r'^jsi18n/$', django_views.i18n.JavaScriptCatalog.as_view(), name='jsi18n'),

    path('', views.InterviewHome, name='InterviewHome'),
    path('Quiz/', views.QuizAddingView, name='quiz'),

    path('AddQuestion/', views.QuestionAndAnswers, name='AddQuestionsWithAnswers'),
    # path('FinalQuiz/', views.Add_Questions, name="AddQuestionToQuiz"),
    path('<slug:slug>', QuizDetailView.as_view(), name="DetailQuiz"),
    path('ViewQuiz/', QuizListView.as_view(), name="ViewQuiz"),
    path('StartQuiz/<slug:slug>', views.StartQuiz, name="StartQuiz"),
    path('StartInterview/<slug:slug>', views.StartInterview, name="StartInterview"),
    path('InterviewQuestions/', views.SaveInterviewQuestions, name="InterQuestions"),
    path('InterviewQuestionDetail/', views.InterviewQuestionDetailView, name="ViewInterViewQuestions"),
    path('interview/', views.InterViewConducting, name="startInterview"),
    path('UserRecord/<slug:slug>', views.GetDetailsForInterview, name="UserForInterview"),
    path('UserApplication/<slug:slug>', views.GetApplicationForInterview, name="UserApplication"),
    path('CSVFile/', views.SaveCsvFile, name="csvSaving"),
    path('RecommendationPannel/',views.systemrecom,name="panel"),
    path('Recommendations/', views.ActualRecommendation, name="recommend"),
    path('UploadingFile/',views.UploadingFile,name="UploadToSystem"),
    re_path(r'^jsi18n/$', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),

]
# path('question/', views.QuestionAdd, name='question'),    # path('Questions/', views.Questions_Detail_view, name="viewQuestions"),
