from rest_framework import serializers
from .models import Category, Course, MCQChoice, MCQQuestion, CourseContent, Enrollment
from django.contrib.auth import get_user_model

User = get_user_model()

class CategorySerializer(serializers.ModelSerializer):
    subcategories = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ["id", "title", "priority", "subcategories"]

    def get_subcategories(self, obj):
        return CategorySerializer(obj.subcategories.all(), many=True).data

class CourseSerializer(serializers.ModelSerializer):
    videos = serializers.SerializerMethodField()
    documents = serializers.SerializerMethodField()
    mcqs = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ["id", "title", "description", "price", "category", "videos", "documents", "mcqs"]

    def get_videos(self, obj):
        return [
            {"id": content.id, "file": content.file.url}
            for content in obj.contents.filter(content_type=CourseContent.VIDEO)
            if content.file
        ]

    def get_documents(self, obj):
        return [
            {"id": content.id, "file": content.file.url}
            for content in obj.contents.filter(content_type=CourseContent.DOCUMENT)
            if content.file
        ]

    def get_mcqs(self, obj):
        return [
            {"id": content.id, "question": content.text}
            for content in obj.contents.filter(content_type=CourseContent.MCQ)
            if content.text
        ]


class MCQChoiceSerializer(serializers.ModelSerializer):
    """Serializer for MCQ Choices"""
    class Meta:
        model = MCQChoice
        fields = ["id", "choice_text", "is_correct"]

class MCQQuestionSerializer(serializers.ModelSerializer):
    """Serializer for MCQ Questions with choices"""
    choices = MCQChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = MCQQuestion
        fields = ["id", "question_text", "choices"]

class EnrolledStudentSerializer(serializers.ModelSerializer):
    """Serializer to return student details"""
    class Meta:
        model = User
        fields = ["id", "email", "first_name", "last_name"]

class CourseEnrollmentSerializer(serializers.ModelSerializer):
    """Serializer to return course details along with enrolled students"""
    students = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ["id", "title", "students"]

    def get_students(self, obj):
        """Fetch students enrolled in the course"""
        enrollments = Enrollment.objects.filter(course=obj)
        students = [enrollment.student for enrollment in enrollments]
        return EnrolledStudentSerializer(students, many=True).data

