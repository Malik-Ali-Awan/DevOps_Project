from file2 import QuoteManager
import pytest

def test_add_and_list_quotes():
    manager = QuoteManager()
    manager.add_quote("Test quote 1.")
    manager.add_quote("Test quote 2.")
    assert manager.list_quotes() == ["Test quote 1.", "Test quote 2."]

def test_search_quotes():
    manager = QuoteManager()
    manager.add_quote("Hard work beats talent.")
    manager.add_quote("Talent is nothing without hard work.")
    results = manager.search_quotes("hard")
    assert len(results) == 2

def test_add_empty_quote():
    manager = QuoteManager()
    with pytest.raises(ValueError):
        manager.add_quote("   ")
