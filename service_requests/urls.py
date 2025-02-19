from django.urls import path
from . import views

app_name = 'service_requests'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('request/new/', views.create_request, name='create_request'),
    path('request/<int:pk>/', views.request_detail, name='request_detail'),
    path('requests/', views.request_list, name='request_list'),
]
