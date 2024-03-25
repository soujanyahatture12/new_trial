# test_calculator.py

from calculator import add, subtract, multiply, divide
import pytest

def test_add():
    result = add(2, 3)
    print(f"Addition result: {result}")
    assert result == 5

    result = add(-1, 1)
    print(f"Addition result: {result}")
    assert result == 0

def test_subtract():
    result = subtract(5, 2)
    print(f"Subtraction result: {result}")
    assert result == 3

    result = subtract(10, 10)
    print(f"Subtraction result: {result}")
    assert result == 0

def test_multiply():
    result = multiply(3, 4)
    print(f"Multiplication result: {result}")
    assert result == 12

    result = multiply(-2, 5)
    print(f"Multiplication result: {result}")
    assert result == -10

def test_divide():
    result = divide(10, 2)
    print(f"Division result: {result}")
    assert result == 5

    result = divide(8, 4)
    print(f"Division result: {result}")
    assert result == 2

def test_divide_by_zero():
    print("Testing division by zero")
    with pytest.raises(ValueError):
        divide(10, 0)
    print("Division by zero test completed")
