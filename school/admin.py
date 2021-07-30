from django.contrib import admin
from school.models.teacher import Teacher
from school.models.group import Group
from school.models.course import Course
from school.models.student import Student
from school.models.enrollment import Enrollment

admin.site.register(Teacher)
admin.site.register(Group)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Enrollment)
