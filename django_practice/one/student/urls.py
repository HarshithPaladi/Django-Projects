from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('students', views.student_dash , name ="student_dashboard"),
    path('students/create_students', views.create_stud , name ="create_student"),
    path('teacher' , views.teacher_dash , name = "teacher_dashboard"),
    path('teacher/create_teachers', views.create_teach, name = "create_teachers"),
    path('courses', views.course_dash , name="course_dashboard"),
    path('courses/create_courses', views.create_enroll , name = "create_enrollment"),
    path('students/<int:studid>' ,views.student_id , name ="studid")
]