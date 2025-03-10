from django.contrib import admin
from django.urls import path, include
from .views import list_books, LibraryDetailView, register, user_login, user_logout
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Add authentication URLs
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
]
