from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient = Ingredient("bacon")
    assert ingredient.name == "bacon"
    assert ingredient.restrictions == {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
    }
    assert repr(ingredient) == "Ingredient('bacon')"
    assert ingredient == Ingredient("bacon")
    assert ingredient != Ingredient("cheese")
    assert hash(ingredient) == hash(Ingredient("bacon"))
    assert hash(ingredient) != hash(Ingredient("cheese"))
    assert isinstance(ingredient, Ingredient)
