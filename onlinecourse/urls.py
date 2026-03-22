from django.urls import path
from . import views

app_name = 'onlinecourse'
urlpatterns = [
    # Path for course details
    path('course/<int:course_id>/', views.submit, name='course_details'),
    # Path for submit view
    path('course/<int:course_id>/submit/', views.submit, name='submit'),
    # Path for exam result view
    path('course/<int:course_id>/submission/<int:submission_id>/result/', 
         views.show_exam_result, name='show_exam_result'),
]
