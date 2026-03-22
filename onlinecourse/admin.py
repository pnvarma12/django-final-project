from django.contrib import admin
from .models import Course, Lesson, Question, Choice, Enrollment, Submission

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']

# Register all models so they appear in the Admin Dashboard
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Submission)
