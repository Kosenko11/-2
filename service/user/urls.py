from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/create/', views.create_request, name='create_request'),
    path('profile/delete/<int:pk>/', views.delete_request, name='delete_request'),
]
