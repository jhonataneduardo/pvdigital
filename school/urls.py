from django.urls import path
from school.views import group, teacher, course

urlpatterns = [
    path('v1/teachers/', teacher.TeacherListCreateAPIView.as_view(), name='list_create_teacher'),
    path('v1/teachers/<int:pk>/', teacher.TeacherRetrieveUpdateDestroyAPIView.as_view(), name='get_update_delete_teacher'),
    path('v1/groups/', group.GroupListCreateAPIView.as_view(), name='list_create_group'),
    path('v1/groups/<int:pk>/', group.GroupRetrieveUpdateDestroyAPIView.as_view(), name='get_update_delete_group'),
    path('v1/courses/', course.CourseListCreateAPIView.as_view(), name='list_create_course'),
    path('v1/courses/<int:pk>/', course.CourseRetrieveUpdateDestroyAPIView.as_view(), name='get_update_delete_course'),
]