from model import Ingredient


def increment(ingredient: Ingredient, new_amount: int):
    return None


def test_increment():
    tomatoes = Ingredient(name="tomatoes", amount=0)
    assert increment(tomatoes, 1) == 0


def test_save():
    tomatoes = Ingredient(name="tomatoes", amount=0)
    tomatoes.save()
