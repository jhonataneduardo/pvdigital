from django.contrib import admin
from socialschool.models.teacher import Teacher
from socialschool.models.course import Course
from socialschool.models.group import Group
from socialschool.models.group import GroupConfig
from socialschool.models.student import Student


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['employee']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'teacher']


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(GroupConfig)
class GroupConfigAdmin(admin.ModelAdmin):
    list_display = ['periods', 'type_vacancies']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'date_of_birth', 'gender', 'active']
