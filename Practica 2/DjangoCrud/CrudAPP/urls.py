from django.urls import path
from CrudAPP import views

urlpatterns = [
    path('', views.teachers, name='teachers'),
    path('create-form/', views.create, name='create'),
    path('update-form/<int:id>', views.update, name='update'),
    path('delete-form/<int:id>', views.delete, name='delete'),
]