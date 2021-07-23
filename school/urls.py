from django.urls import path
from school.views.teacher import TeacherListCreateAPIView, TeacherRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('v1/teachers/', TeacherListCreateAPIView.as_view(), name='list_create_teacher'),
    path('v1/teachers/<int:pk>/', TeacherRetrieveUpdateDestroyAPIView.as_view(), name='get_update_delete_teacher'),
]