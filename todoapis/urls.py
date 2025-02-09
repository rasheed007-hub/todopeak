from django.urls import path
from . import views

urlpatterns = [
    path('', views.TodoView.as_view()),
    path('todo/<int:id>/', views.TodoDetailView.as_view())
]