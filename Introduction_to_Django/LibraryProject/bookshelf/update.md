# Updating a Book

To update a book’s author, use:

```python
book = Book.objects.filter(title="1984").first()
book.author = "G. Orwell"
book.save()
print(f"Updated: {book.title}, {book.author}, {book.publication_year}")
