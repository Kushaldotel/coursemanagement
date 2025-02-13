from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Category, Course, CourseContent, MCQQuestion, MCQChoice, Enrollment

@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ("title", "priority", "parent")
    search_fields = ("title",)
    list_filter = ("parent",)
    ordering = ["priority"]

@admin.register(Course)
class CourseAdmin(ModelAdmin):
    list_display = ("title", "category", "price", "instructor")
    search_fields = ("title", "instructor__email")
    list_filter = ("category",)
    ordering = ["-price"]
    autocomplete_fields = ["category", "instructor"]

@admin.register(CourseContent)
class CourseContentAdmin(ModelAdmin):
    list_display = ("course", "content_type")
    list_filter = ("content_type",)
    search_fields = ("course__title",)
    ordering = ["course"]

    fieldsets = (
        ("Course Content", {
            "fields": ("course", "content_type", "file", "text"),
        }),
    )

@admin.register(MCQQuestion)
class MCQQuestionAdmin(ModelAdmin):
    list_display = ("course_content", "question_text")
    search_fields = ("question_text",)
    ordering = ["course_content"]

@admin.register(MCQChoice)
class MCQChoiceAdmin(ModelAdmin):
    list_display = ("question", "choice_text", "is_correct")
    list_filter = ("is_correct",)
    search_fields = ("choice_text",)
    ordering = ["question"]

@admin.register(Enrollment)
class EnrollmentAdmin(ModelAdmin):
    list_display = ("student", "course", "enrolled_at", "progress", "is_completed")
    search_fields = ("student__email", "course__title")
    list_filter = ("is_completed", "course")
    ordering = ["-enrolled_at"]
    autocomplete_fields = ["student", "course"]
    actions = ["mark_as_completed"]

    def mark_as_completed(self, request, queryset):
        queryset.update(is_completed=True, progress=100)
        self.message_user(request, "Selected enrollments marked as completed!")
    mark_as_completed.short_description = "Mark selected enrollments as completed"