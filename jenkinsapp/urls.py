from django.urls import path
from jenkinsapp.views import create_student

urlpatterns = [
    path('', create_student, name = 'create-student')
]