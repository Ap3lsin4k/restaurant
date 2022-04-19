from dataclasses import dataclass


@dataclass
class Ingredient:
    name: str
    amount: int


@dataclass
class Food:
    ingredients: [Ingredient]