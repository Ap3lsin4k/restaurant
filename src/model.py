from dataclasses import dataclass


@dataclass
class Ingredient:
    name: str
    amount: int


@dataclass
class Food:
    ingredients: [Ingredient]


@dataclass
class Storage:
    ingredients: [Ingredient]
