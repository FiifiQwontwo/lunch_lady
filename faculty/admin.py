from django.contrib import admin
from .models import Faculty
from course.models import Course
# Register your models here.

admin.site.site_header = "Lunch Lady"
admin.site.site_title = "Lunch Lady Admin"
admin.site.index_title = "Lunch Lady"

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    search_fields = ['faculty_name']
    list_per_page = 20
    prepopulated_fields = {'slug': ('faculty_name',)}



@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    search_fields = ['faculty', 'course_name']
    list_display=['course_name', 'faculty']
    list_per_page = 20
    prepopulated_fields = {'slug': ('course_name',)}



