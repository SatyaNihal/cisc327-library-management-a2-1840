import pytest 

from library_service import borrow_book_by_patron, return_book_by_patron

def test_return_discrete_math():
    # return discrete math book -> not implemented yet
    success, msg = return_book_by_patron("333333", 1)
    assert success == False

def test_return_wrong_patron():
    # patron 444444 tries to return book borrowed by 555555
    borrow_book_by_patron("555555", 1)
    success, msg = return_book_by_patron("444444", 1)
    assert success == False

def test_return_already_returned():
    # return a book that was already returned
    borrow_book_by_patron("666666", 1)
    return_book_by_patron("666666", 1)
    success, msg = return_book_by_patron("666666", 1)
    assert success == False

def test_return_negative_book_id():
    # negative book id -> should fail
    success, msg = return_book_by_patron("123456", -1)
    assert success == False

def test_return_patron_id_short():
    # patron id only 4 digits -> should fail
    success, msg = return_book_by_patron("1234", 1)
    assert success == False