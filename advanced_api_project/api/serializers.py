from rest_framework import serializers
from .models import Author, Book
import datetime

class BookSerializer(serializers.ModelSerializer):
    """
    Serializes all fields of the Book model.
    Adds custom validation for publication_year to ensure it's not in the future.
    """
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        current_year = datetime.datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes the Author model along with its related books using nested serialization.
    The 'books' field is populated with data from BookSerializer.
    """
    books = BookSerializer(many=True, read_only=True) # nested relationship using related_name='books'

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']