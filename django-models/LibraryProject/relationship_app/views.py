from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from .models import Book
from django.views.generic.detail import DetailView
from .models import Library
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

# User Registration View
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

# Class-Based View to show details of a specific Library
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html" 
    context_object_name = "library"

def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(is_admin, login_url='/login/')
def admin_view(request):
    return HttpResponse("Welcome to the Admin Dashboard.")

@user_passes_test(is_librarian)
def librarian_view(request):
    return HttpResponse("Welcome to the Librarian Panel.")

@user_passes_test(is_member)
def member_view(request):
    return HttpResponse("Welcome to the Member Section.")