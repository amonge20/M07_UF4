from django.contrib import admin
from django.urls import path
from centre import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('students/', views.studentsApp, name="studentsApp"),
    path('teachers/', views.teachersApp, name="teachersApp"),
    path('studentsProject/', views.studentsProject, name="studentsProject"),
    path('teachersProject/', views.teachersProject, name="teachersProject"),
    path('students/student/<str:pk>', views.alumne, name="alumne"),
    path('teachers/teacher/<str:pk>', views.profesor, name="profesor")
]