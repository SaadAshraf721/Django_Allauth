from django.urls import path

from adminapp import views

urlpatterns = [
    path('', views.add_exam),
    path('all-exam/', views.all_exam),
]
