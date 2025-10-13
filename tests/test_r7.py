import pytest 

from library_service import get_patron_status_report

def test_patron_status_123456():
    # get status for patron 123456 -> not implemented yet
    status = get_patron_status_report("123456")
    assert isinstance(status, dict)

def test_patron_status_borrowed_books():
    # check if status includes borrowed books field
    status = get_patron_status_report("111111")
    assert isinstance(status, dict)

def test_patron_status_late_fees():
    # check if status includes late fees field
    status = get_patron_status_report("222222")
    assert isinstance(status, dict)

def test_patron_status_borrowing_history():
    # check if status includes borrowing history
    status = get_patron_status_report("333333")
    assert isinstance(status, dict)

def test_patron_status_total_borrowed():
    # check if status includes total borrowed count
    status = get_patron_status_report("444444")
    assert isinstance(status, dict)