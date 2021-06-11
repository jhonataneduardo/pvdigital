from django.contrib import admin
from socialschool.models.teacher import Teacher
from socialschool.models.course import Course
from socialschool.models.group import Group


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['employee']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'teacher']


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['name']
