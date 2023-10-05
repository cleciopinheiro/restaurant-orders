from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
import pytest


# Req 2
def test_dish():
    instance = Dish('Morango', 5.4)
    another_instance = Dish('Palmito', 4.90)

    assert instance.name == 'Morango'

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish('a', '3')

    error = "Dish price must be greater then zero."
    with pytest.raises(ValueError, match=error):
        Dish('a', -3)

    assert repr(instance) == "Dish('Morango', R$5.40)"
    assert instance == instance
    assert instance != another_instance
    assert hash(instance) == hash(repr(instance))
    assert hash(instance) != hash(repr(another_instance))

    instance.add_ingredient_dependency(Ingredient('Água'), 3)
    assert instance.recipe == {Ingredient('Água'): 3}
    assert instance.get_ingredients() == set(instance.recipe.keys())
    assert instance.get_restrictions() == set()
