from django.urls import path, include

from. import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('contactUS/', views.contact, name="who"),
    path('register/', views.signup, name="signup"),
    path('abc/', views.ind, name='ind')
]
