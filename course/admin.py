from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Category, Course, CourseContent, MCQQuestion, MCQChoice

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
