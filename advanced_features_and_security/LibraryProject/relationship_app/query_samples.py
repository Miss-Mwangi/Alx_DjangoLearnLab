from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author_name = "Author Name"
try:
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)
    print("Books by", author_name, ":", [book.title for book in books_by_author])
except Author.DoesNotExist:
    print(f"No author found with the name {author_name}")
    
# List all books in a library
library_name = "Library Name"
try:
    library = Library.objects.get(name=library_name)
    books_in_library = library.books.all()
    print("Books in", library_name, ":", [book.title for book in books_in_library])
except Library.DoesNotExist:
    print(f"No library found with the name {library_name}")

# Retrieve the librarian for a library
library_name = "Library Name"
try:
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    print(f"The librarian for {library_name} is {librarian.name}")
except (Library.DoesNotExist, Librarian.DoesNotExist):
    print(f"No librarian found for {library_name}")
