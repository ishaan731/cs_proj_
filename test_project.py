import pytest
from project import recommend_books, load_books, visualize_recs

def test_recommend_books():
    assert "The Alchemist" in recommend_books("inspiring")
    assert "To Kill a Mockingbird" in recommend_books("sad")
    assert "1984" in recommend_books("thought-provoking")
    assert "Pride and Prejudice" in recommend_books("happy")

def test_recommend_books_no_match():
    assert recommend_books("angry") == []

def test_load_books():
    books = load_books()
    assert isinstance(books, dict)
    assert "The Alchemist" in books
    assert "Great Gatsby" in books
    assert "Dracula" in books

def test_visualize_recs():
    try:
        visualize_recs(["The Alchemist", "1984"])
        assert True
    except:
        assert False

if __name__ == "__main__":
    pytest.main()
