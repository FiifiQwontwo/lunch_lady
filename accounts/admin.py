from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(CustomUser)
admin.site.register(UserAgentInfo)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('index_number', 'level', 'course')
    list_filter = ('level', 'course')
    search_fields = ('index_number',)
    fieldsets = ()


admin.site.register(Student, StudentAdmin)

@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    list_display = ('faculty',)
    list_filter = ('faculty',)
    search_fields = ('faculty',)
    fieldsets = ()