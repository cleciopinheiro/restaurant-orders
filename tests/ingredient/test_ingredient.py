from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    instance = Ingredient('milk')
    instance2 = Ingredient('chocolate')

    assert instance.name == 'milk'
    assert hash(instance) == hash('milk')
    assert repr(instance) == "Ingredient('milk')"
    assert instance == instance
    assert instance != instance2
    assert instance.restrictions == set()
