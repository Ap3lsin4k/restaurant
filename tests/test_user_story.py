import pytest

from model import Ingredient, Food, Order


def increment(ingredient: Ingredient, new_amount: int) -> None:
    ingredient.amount = 1
    return 0


def test_increment():
    tomatoes = Ingredient(name="tomatoes", amount=0)
    assert increment(tomatoes, 1) == 0
    assert tomatoes.amount == 1


def test_save():
    tomatoes = Ingredient(name="tomatoes", amount=0)
    tomatoes.save()


@pytest.fixture
def pancakes():
    wheat = Ingredient(name="wheat", amount=150)
    water = Ingredient(name="water", amount=150)
    pancakes = Food((wheat, water))
    return pancakes


def test_create_food(pancakes):
    order = Order(pancakes)
    assert order.num_of_guests == 0
    order.increment()
    assert order.num_of_guests == 1


def test_increment_order():
    dummy = None
    order = Order(dummy)
    order.increment()
    order.increment()
    assert order.num_of_guests == 2

    order.increment(5)
    assert order.num_of_guests == 7


def test_calculate_ingredients_from_order():
    wheat = Ingredient(name="wheat", amount=150)
    meal = Food((wheat,))
    order = Order(meal)
    assert order.all_ingredients == dict()

    order.increment()
    assert order.all_ingredients == {"wheat": 150}

    order.increment()
    assert order.all_ingredients == {"wheat": 300}


def test_calculate(pancakes):
    order = Order(pancakes)
    order.increment()
    assert order.all_ingredients == {"wheat": 150, "water": 150}
