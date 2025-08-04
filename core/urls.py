from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/categories/', permanent=False)),
    path('categories/', views.category_list, name='category_list'),
    path('categories/create/', views.category_create, name='category_create'),
    path('categories/<int:pk>/edit/', views.category_update, name='category_update'),
    path('categories/<int:pk>/delete/', views.category_delete, name='category_delete'),
    path('categories/<int:pk>/', views.category_detail, name='category_detail'),
    path('courses/', views.course_list, name='course_list'),
    path('courses/create/', views.course_create, name='course_create'),
    path('courses/<int:pk>/edit/', views.course_update, name='course_update'),
    path('courses/<int:pk>/delete/', views.course_delete, name='course_delete'),
    path('courses/<int:pk>/', views.course_detail, name='course_detail'), 
]







# mansura
# maha0145@gmail.com
# maha0514 


# Sarah_Johnson - password= password123
# David Lee- password= password345
# Priya_Desai- password='password567 
# Ahmad_Khan- password= password789 
# Lisa_Wang- password= password987 
# Jason_Smith- password= password765 
# Elena Petrova- password= passwor543 
# Mark Robinson- password= password321
