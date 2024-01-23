from django.urls import path

from . import views


urlpatterns = [
    
    path('', views.homepage),
    path('schoolperdistrict/', views.school1),
    path('schoolcatperdistrict/', views.school2),
    path('languageperdistrict/', views.school3),
]
