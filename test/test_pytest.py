import pytest
from src import calculator

def test_fun1():
    assert calculator.fun1(2, 3) == 5
    assert calculator.fun1(5,0) == 5
    assert calculator.fun1 (-1, 1) == 0
    assert calculator.fun1 (-1, -1) == -2


def test_fun2():
    assert calculator.fun2(2, 3) == -1
    assert calculator.fun2(5,0) == 5
    assert calculator.fun2 (-1, 1) == -2
    assert calculator.fun2 (-1, -1) == 0

def test_fun3():
    assert calculator.fun3(2, 3) == 6
    assert calculator.fun3(5,0) == 0
    assert calculator.fun3 (-1, 1) == -1
    
    assert calculator.fun3 (-1, -1) == 1

def test_fun4():
    assert calculator.fun4(2, 3, 5) == 10
    assert calculator.fun4(5,0, -1) == 4
    assert calculator.fun4 (-1, -1, -1) == -3
    assert calculator.fun4 (-1, -1, 100) == 98

def test_fun5():
    assert calculator.fun5(10, 3) == 1
    assert calculator.fun5(7, 2) == 1
    assert calculator.fun5(9, 3) == 0
    assert calculator.fun5(-7, 3) == 2

def test_fun5_zero_division():
    with pytest.raises(ValueError):
        calculator.fun5(5, 0)

def test_fun6():
    assert calculator.fun6(2, 3) == 8
    assert calculator.fun6(5, 0) == 1
    assert calculator.fun6(3, 3) == 27
    assert calculator.fun6(-2, 3) == -8
