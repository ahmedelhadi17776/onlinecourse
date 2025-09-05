from django.contrib import admin
from .models import Course, Instructor, Lesson, Question, Choice, Submission

# Register your models here.


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'order']


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name']


class InstructorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'user')


class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('enrollment', 'lesson', 'date')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Choice)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Submission, SubmissionAdmin)
