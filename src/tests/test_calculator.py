"""
Calculator app tests
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

from src.calculator import Calculator

def test_app():
    my_calculator = Calculator()
    assert my_calculator.get_hello_message() == "== Calculatrice v1.0 =="


# TODO: ajoutez les tests
def test_addition():
    my_calculator = Calculator()
    assert my_calculator.addition(2, 3) == 5
    assert my_calculator.addition(-1, 1) == 0


def test_soustraction():
    my_calculator = Calculator()
    assert my_calculator.subtraction(2, 3) == -1
    assert my_calculator.subtraction(5, 2) == 3
    assert my_calculator.subtraction(0, 5) == -5


def test_multiplication():
    my_calculator = Calculator()
    assert my_calculator.multiplication(2, 3) == 6
    assert my_calculator.multiplication(-2, 3) == -6
    assert my_calculator.multiplication(0, 10) == 0


def test_division():
    my_calculator = Calculator()
    assert my_calculator.division(6, 3) == 2
    assert my_calculator.division(-6, 3) == -2
    assert my_calculator.division(0, 3) == 0


def test_division_by_zero():
    my_calculator = Calculator()
    assert my_calculator.division(5, 0) == "Erreur : division par zéro"
    assert my_calculator.last_result == "Error"