from django.contrib import admin
from django.urls import path
from .views import subjectupdate, 

urlpatterns = [
    path('', )
    path('task/edit/<str:pk>/', subjectupdate.as_view(), name='task_update')
]