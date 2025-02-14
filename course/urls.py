from django.urls import path
from .views import CategoryListView, CourseListView, MCQQuestionListAPIView,MCQQuestionByCourseAPIView,CourseEnrollmentListAPIView

urlpatterns = [
    path("categories/", CategoryListView.as_view(), name="category-list"),
    path("courses/", CourseListView.as_view(), name="course-list"),
    path("mcqs/", MCQQuestionListAPIView.as_view(), name="mcq-list"),
    path("mcqs/<int:course_id>/", MCQQuestionByCourseAPIView.as_view(), name="mcq-by-course"),
    path("enrollments/", CourseEnrollmentListAPIView.as_view(), name="course-enrollments"),
]
