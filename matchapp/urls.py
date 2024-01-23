from django.urls import path

from . import views


urlpatterns = [
    path('', views.homepage),
    path('match1/', views.match1),
    path('match2/', views.match2),
]