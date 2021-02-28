from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("test1/", views.index_template, name="index_template"),
    path("exercise/", views.exercise, name="exercise"),
    path("exercise2/", views.exercise_class.as_view(), name="exercise_class"),
]
