from django.contrib import admin
from school.models.teacher import Teacher
from school.models.group import Group
from school.models.course import Course
from school.models.student import Student

admin.site.register(Teacher)
admin.site.register(Group)
admin.site.register(Course)
admin.site.register(Student)
