import pytest 

from library_service import calculate_late_fee_for_book

def test_late_fee_semiotics_book():
    # calculate fee for semiotics book -> not implemented
    result = calculate_late_fee_for_book("777777", 1)
    assert isinstance(result, dict)
    assert 'fee_amount' in result
    assert 'days_overdue' in result
    assert 'status' in result

def test_late_fee_operating_systems():
    # calculate fee for operating systems book
    result = calculate_late_fee_for_book("888888", 1)
    assert isinstance(result, dict)
    assert 'fee_amount' in result
    assert 'days_overdue' in result
    assert 'status' in result

def test_late_fee_discrete_math():
    # calculate fee for discrete math book
    result = calculate_late_fee_for_book("999999", 1)
    assert isinstance(result, dict)
    assert 'fee_amount' in result
    assert 'days_overdue' in result
    assert 'status' in result

def test_late_fee_patron_id_none():
    # patron id is None -> should handle gracefully
    result = calculate_late_fee_for_book(None, 1)
    assert isinstance(result, dict)
    assert 'fee_amount' in result
    assert 'days_overdue' in result
    assert 'status' in result

def test_late_fee_book_id_string():
    # book id is string instead of int -> should handle
    result = calculate_late_fee_for_book("123456", "1")
    assert isinstance(result, dict)
    assert 'fee_amount' in result
    assert 'days_overdue' in result
    assert 'status' in result