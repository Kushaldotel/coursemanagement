from rest_framework import generics
from .models import Category, Course, MCQQuestion
from .serializers import CategorySerializer, CourseSerializer, MCQChoiceSerializer, MCQQuestionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# 🔹 Category List API
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.filter(parent=None)
    serializer_class = CategorySerializer

# 🔹 Course List API
class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# 🔹 MCQ List API for a Specific Course
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
