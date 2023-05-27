from src.models.dish import Dish
from src.models.ingredient import Ingredient  # noqa: F401, E261, E501
import pytest


# Req 2
def test_dish():
    ingredient1 = Ingredient("Tomato")

    dish_spaghetti = Dish("Spaghetti", 9.99)
    dish_lasagna = Dish("Lasagna", 12.99)

    assert dish_spaghetti.name == "Spaghetti"
    assert hash(dish_spaghetti) == hash(Dish("Spaghetti", 9.99))
    assert hash(dish_spaghetti) != hash(dish_lasagna)
    assert dish_spaghetti == dish_spaghetti
    assert dish_spaghetti.name != dish_lasagna.name
    assert repr(dish_spaghetti) == "Dish('Spaghetti', R$9.99)"

    dish_spaghetti.add_ingredient_dependency(ingredient1, 2)

    assert set(dish_spaghetti.get_ingredients()) == {ingredient1}
    assert dish_spaghetti.get_restrictions() == set()

    with pytest.raises(TypeError):
        Dish("Pizza", "10.99")

    with pytest.raises(ValueError):
        Dish("Burger", -5.99)
