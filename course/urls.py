from django.urls import path
from . import views

app_name = 'course'

urlpatterns = [
    # Course views
    path('', views.index, name='index'),
    path('<int:course_id>/', views.course_detail, name='detail'),
    path('<int:course_id>/detail/', views.course_detail, name='course_detail'),

    # Assessment views
    path('<int:lesson_id>/submit/', views.submit, name='submit'),
    path('<int:lesson_id>/result/<int:submission_id>/',
         views.show_exam_result, name='show_exam_result'),

    # Authentication views
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.user_signup, name='signup'),
]
