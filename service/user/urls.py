from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("main/", views.index, name="index"),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/create/', views.create_request, name='create_request'),
    path('dashboard/requests/', views.request_list, name='request_list'),
    path('dashboard/requests/<int:pk>/delete/', views.delete_request, name='delete_request'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

