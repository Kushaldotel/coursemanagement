from rest_framework import generics
from .models import Category, Course, MCQQuestion
from .serializers import CategorySerializer, CourseSerializer, MCQChoiceSerializer, MCQQuestionSerializer,CourseEnrollmentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.filter(parent=None)
    serializer_class = CategorySerializer

class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class MCQQuestionListAPIView(generics.ListAPIView):
    """API View to get all MCQ questions with choices"""
    queryset = MCQQuestion.objects.all()
    serializer_class = MCQQuestionSerializer


class MCQQuestionByCourseAPIView(generics.ListAPIView):
    """API View to get MCQ questions for a specific course"""
    serializer_class = MCQQuestionSerializer

    def get_queryset(self):
        course_id = self.kwargs["course_id"]
        return MCQQuestion.objects.filter(course_content__course_id=course_id)

class CourseEnrollmentListAPIView(generics.ListAPIView):
    """API View to fetch all courses with enrolled students"""
    queryset = Course.objects.all()
    serializer_class = CourseEnrollmentSerializer


def course_enrollment_page(request):
    """View to render the course enrollment page"""
    return render(request, "enrollments.html")
