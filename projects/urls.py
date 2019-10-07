from django.urls import path

from . import views

urlpatterns = [
    path('', views.allprojects, name='allprojects'),
    path('<int:project_id>/', views.detail, name='detail'),
]