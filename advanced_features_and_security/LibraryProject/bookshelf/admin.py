from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Book

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("username", "email", "role", "is_staff", "is_active")
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("date_of_birth", "profile_photo", "role")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Info", {"fields": ("date_of_birth", "profile_photo", "role")}),
    )

admin.site.register(CustomerUser, CustomUserAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('publication_year', 'author')
    search_fields = ('title', 'author')

admin.site.register(Book, BookAdmin)
