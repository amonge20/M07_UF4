from django.urls import path
from centre import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
]