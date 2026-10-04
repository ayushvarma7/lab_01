import pytest
from src import calculator

def test_fun1():
    assert calculator.fun1(2, 4) == 6
    assert calculator.fun1(5,-1) == 4
    assert calculator.fun1(-1, 1) == 0
    assert calculator.fun1(-1, -1) == -2
