import pytest 

from library_service import search_books_in_catalog

def test_search_science_keyword():
    # search for "science" in title -> not implemented yet
    results = search_books_in_catalog("science", "title")
    assert isinstance(results, list)

def test_search_silberschatz_author():
    # search for author "silberschatz"
    results = search_books_in_catalog("silberschatz", "author")
    assert isinstance(results, list)

def test_search_operating_systems_isbn():
    # search by operating systems isbn
    results = search_books_in_catalog("9781119320913", "isbn")
    assert isinstance(results, list)

def test_search_ken_author():
    # search for "ken" in author name
    results = search_books_in_catalog("ken", "author")
    assert isinstance(results, list)

def test_search_invalid_type():
    # search type is invalid -> should handle gracefully
    results = search_books_in_catalog("test", "invalid")
    assert isinstance(results, list)