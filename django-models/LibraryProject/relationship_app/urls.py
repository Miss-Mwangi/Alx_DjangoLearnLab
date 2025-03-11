from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import register
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books, LibraryDetailView 


urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Add authentication URLs
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]
