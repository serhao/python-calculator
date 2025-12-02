# test_calculator.py

import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    """Test addition function."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    """Test subtraction function."""
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5
    assert subtract(-3, -2) == -1

def test_multiply():
    """Test multiplication function."""
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6
    assert multiply(0, 5) == 0

def test_divide():
    """Test division function."""
    assert divide(8, 2) == 4
    assert divide(9, 3) == 3
    assert divide(-10, 2) == -5

@pytest.mark.edge
def test_divide_by_zero():
    """Test that dividing by zero raises an error."""
    with pytest.raises(ValueError):
        divide(10, 0)

@pytest.mark.edge
def test_large_numbers():
    """Test with large numbers."""
    assert add(1000000, 2000000) == 3000000
    assert multiply(10000, 10000) == 100000000

@pytest.mark.edge
def test_negative_edge_cases():
    """Test edge cases with negative numbers."""
    assert divide(-100, -10) == 10
    assert subtract(-5, -10) == 5

@pytest.mark.slow
def test_performance_add():
    """Test addition performance with many operations."""
    result = 0
    for i in range(100000):
        result = add(result, 1)
    assert result == 100000

@pytest.mark.slow
def test_performance_multiply():
    """Test multiplication performance."""
    result = 1
    for i in range(1000):
        result = multiply(result, 1)
    assert result == 1

