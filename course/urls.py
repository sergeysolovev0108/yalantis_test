from django.urls import path, include
from course.views import *

urlpatterns = [
    path('course/create/', CourseCreateView.as_view()),
    path('all/', CourseListView.as_view()),
    path('deteil/<int:pk>/', CourseDetailView.as_view()),
]
