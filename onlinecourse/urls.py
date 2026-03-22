from django.urls import path
from . import views

app_name = 'onlinecourse'
urlpatterns = [
    # This matches the page in your screenshot
    path('course/<int:course_id>/', views.submit, name='course_details'),
    # This is where the "Take Exam" button goes
    path('course/<int:course_id>/submit/', views.submit, name='submit'),
    # This is the result page
    path('course/<int:course_id>/submission/<int:submission_id>/result/', 
         views.show_exam_result, name='show_exam_result'),
]
