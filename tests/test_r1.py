import pytest 

from library_service import add_book_to_catalog

def test_add_book_semiotics():
    # adding the semiotics textbook -> should work
    success, msg = add_book_to_catalog("Semiotics: The Science of Signs", "Donato Santeramo", "9783862902279", 3)
    assert success is True
    assert "semiotics" in msg.lower()

def test_add_book_empty_author():
    # author field is empty -> should fail
    success, msg = add_book_to_catalog("Canadian Law: An Introduction, 8th Edition", "", "9781119320913", 2)
    assert success is False
    assert "author" in msg.lower()

def test_add_book_zero_copies():
    # zero copies not allowed -> should fail
    success, msg = add_book_to_catalog("Discrete Math and its Applications", "Kenneth H. Rosen", "9781259676512", 0)
    assert success is False
    assert "positive" in msg.lower()

def test_add_book_author_too_long():
    # author name over 100 chars -> should reject
    long_author = "A" * 101
    success, msg = add_book_to_catalog("Canadian Law: An Introduction, 8th Edition", long_author, "9783862902279", 1)
    assert success is False
    assert "author" in msg.lower()

def test_add_book_isbn_with_letters():
    # isbn contains letters -> should fail
    success, msg = add_book_to_catalog("Canadian Law: An Introduction, 8th Edition", "Emond Publishing", "978abc1234567", 1)
    assert success is False
    assert "13 digits" in msg