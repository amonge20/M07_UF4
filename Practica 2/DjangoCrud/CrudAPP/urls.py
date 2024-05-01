from django.urls import path
from CrudAPP import views

urlpatterns = [
    path('', views.users, name='users'),
    path('create-form/', views.create, name='create'),
    path('update-form/<int:pk>', views.update, name='update'),
    path('delete-form/<int:pk>', views.delete, name='delete'),
]