from django.urls import path

from . import views

urlpatterns = [
    path('school/', views.SchoolAPIView.as_view()),
    path('class/', views.ClassAPIView.as_view()),
    path('student/', views.StudentAPIView.as_view()),
    path('teacher/', views.TeacherAPIView.as_view()),
    path('subject/', views.SubjectAPIView.as_view()),
    path('class_search/', views.ClassSearchAPIView.as_view()),
    path('class_student/', views.ClassStudentAPIView.as_view()),
]
