from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

# from . views import (
#     detail
# )

app_name = 'UserViews'
urlpatterns = [
    path('', views.UserHome, name="UserHome"),
    path('page/', views.testing, name="testing"),
    path('application/', views.application, name="application"),
    path('profile/', views.detailView, name='Profile'),
    path('<str:user>', views.detailView2, name='Profile2'),
    path('test/', views.test, name="test"),
    path('update/<int:id>/', views.Application_update_view, name="Update"),
    path('<int:id>/delete/', views.Application_Delete_view, name='Delete'),
    # path('QuizManager/', views.QuizManager, name="QuizManager"),
    path('Quiz/', views.QuizPortal, name="GetQuiz"),
    path('<slug:slug>/', views.GetQuestions, name="GetQuestions"),
    path('/saved', views.MarkQuiz, name='MarkQuiz'),
    path('/category/', views.GradePortal, name='category'),
    path('Grades/<slug:slug>/', views.GradeShow, name='ShowGrade')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
