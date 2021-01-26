from . import views
from django.urls import path

urlpatterns = [
    path('', views.project_index, name="PIndex"),
    path('<int:pk>/', views.projet_detail, name='PDetail')
]