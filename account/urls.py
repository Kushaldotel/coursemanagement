from django.urls import path
from .views import CreateStudentView, create_student_page

urlpatterns = [
    path('create-student/', CreateStudentView.as_view(), name='create-student'),
    path('create-student-page/', create_student_page, name='create-student-page'),  # URL for the frontend form
]
