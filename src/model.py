from dataclasses import dataclass
from typing import Dict


@dataclass
class Ingredient:
    name: str
    amount: int

    def save(self):
        pass


@dataclass
class Food:
    ingredients: [Ingredient]


@dataclass
class Storage:
    ingredients: [Ingredient]


class Order:
    meal: Food
    num_of_guests: int

    def __init__(self, meal):
        self.meal = meal
        self.num_of_guests = 0

    def increment(self, new_guests=1) -> None:
        self.num_of_guests += new_guests

    @property
    def all_ingredients(self) -> Dict[str, int]:
        ingredients = dict()

        if not self.num_of_guests:
            return ingredients

        for ingredient in self.meal.ingredients:
            ingredients[ingredient.name] = ingredient.amount * self.num_of_guests
        return ingredients
