from relationship_app.models import Author, Book

# Query all books by a specific author
author_name = "Author Name"
author = Author.objects.filter(name=author_name).first()

if author:
    books_by_author = Book.objects.filter(author=author)
    print("Books by", author_name, ":", [book.title for book in books_by_author])
else:
    print(f"No author found with the name {author_name}")

# List all books in a library
library_name = "Library Name"
library = Library.objects.filter(name=library_name).first()

if library:
    books_in_library = library.books.all()
    print("Books in", library_name, ":", [book.title for book in books_in_library])
else:
    print(f"No library found with the name {library_name}")

# Retrieve the librarian for a library
library_name = "Library Name"
library = Library.objects.filter(name=library_name).first()

if library:
    librarian = Librarian.objects.filter(library=library).first()
    if librarian:
        print(f"The librarian for {library_name} is {librarian.name}")
    else:
        print(f"No librarian found for {library_name}")

else:
    print(f"No library found with the name {library_name}")


