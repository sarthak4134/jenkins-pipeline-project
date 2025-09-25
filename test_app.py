from app import add

def test_add_positive_numbers():
    """Tests addition of two positive numbers."""
    assert add(2, 3) == 5

def test_add_negative_numbers():
    """Tests addition of two negative numbers."""
    assert add(-1, -1) == -2