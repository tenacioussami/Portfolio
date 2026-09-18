from django.urls import path
from . import views

app_name = 'my_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.project_list, name='project_list'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('about/', views.about, name='about'),
]
