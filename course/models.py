from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    """Category Model with two-level hierarchy"""
    title = models.CharField(max_length=255, unique=True)
    priority = models.IntegerField(default=0)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="subcategories"
    )  # Allows for two-level categorization

    def __str__(self):
        return self.title

class Course(models.Model):
    """Course model with title, description, price, and category"""
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="courses")
    instructor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="courses") # Future Instructor System

    def __str__(self):
        return self.title

class CourseContent(models.Model):
    """Course Content (Videos, Documents, MCQs)"""
    VIDEO = "video"
    DOCUMENT = "document"
    MCQ = "mcq"

    CONTENT_TYPES = [
        (VIDEO, "Video"),
        (DOCUMENT, "Document"),
        (MCQ, "MCQ Quiz"),
    ]

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="contents")
    content_type = models.CharField(max_length=10, choices=CONTENT_TYPES)
    file = models.FileField(upload_to="course_files/", blank=True, null=True)  # Video & Document
    text = models.TextField(blank=True, null=True)  # MCQ Text Content

    def __str__(self):
        return f"{self.course.title} - {self.content_type}"

    def save(self, *args, **kwargs):
        """File validation based on type"""
        if self.content_type == self.VIDEO:
            if self.file.size > 50 * 1024 * 1024:  # 50MB limit
                raise ValueError("Video file size exceeds 50MB")
            if not self.file.name.endswith('.mp4'):
                raise ValueError("Only MP4 format allowed for videos.")
        elif self.content_type == self.DOCUMENT:
            if self.file.size > 10 * 1024 * 1024:  # 10MB limit
                raise ValueError("Document file size exceeds 10MB")
            if not self.file.name.endswith('.pdf'):
                raise ValueError("Only PDF format allowed for documents.")
        super().save(*args, **kwargs)

class MCQQuestion(models.Model):
    """MCQ Question Model"""
    course_content = models.ForeignKey(CourseContent, on_delete=models.CASCADE, related_name="mcq_questions")
    question_text = models.TextField()

    def __str__(self):
        return self.question_text

class MCQChoice(models.Model):
    """MCQ Choices Model"""
    question = models.ForeignKey(MCQQuestion, on_delete=models.CASCADE, related_name="choices")
    choice_text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)  # Multiple correct answers allowed

    def __str__(self):
        return f"{self.choice_text} - {'Correct' if self.is_correct else 'Incorrect'}"


class Enrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="enrollments")
    course = models.ForeignKey("Course", on_delete=models.CASCADE, related_name="enrollments")
    enrolled_at = models.DateTimeField(auto_now_add=True)
    progress = models.FloatField(default=0.0)  # Track progress percentage
    is_completed = models.BooleanField(default=False)

    class Meta:
        unique_together = ("student", "course")  # Prevent duplicate enrollments
        ordering = ["-enrolled_at"]

    def __str__(self):
        return f"{self.student.email} -> {self.course.title}"
