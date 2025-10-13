import pytest 

from database import get_all_books

def test_catalog_returns_list():
    # catalog should return a list of books
    books = get_all_books()
    assert isinstance(books, list)

def test_catalog_book_has_id():
    # each book should have an id field
    books = get_all_books()
    if books:
        assert "id" in books[0]

def test_catalog_book_has_total_copies():
    # each book should show total copies
    books = get_all_books()
    if books:
        assert "total_copies" in books[0]

def test_catalog_book_has_available_copies():
    # each book should show available copies
    books = get_all_books()
    if books:
        assert "available_copies" in books[0]

def test_catalog_books_ordered():
    # books should be in some order (title order)
    books = get_all_books()
    if len(books) > 1:
        titles = [book["title"] for book in books]
        assert titles == sorted(titles)