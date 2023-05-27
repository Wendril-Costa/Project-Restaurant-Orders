import csv
from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.ingredients = set()

        with open(source_path, newline="") as file:
            reader = csv.DictReader(file)
            dish_ingredients_map = {}

            for row in reader:
                dish_name = row["dish"]
                dish_price = float(row["price"])
                ingredient_name = row["ingredient"]
                ingredient_quantity = int(row["recipe_amount"])

                ingredient = Ingredient(ingredient_name)
                self.ingredients.add(ingredient)

                if dish_name not in dish_ingredients_map:
                    dish = Dish(dish_name, dish_price)
                    dish_ingredients_map[dish_name] = dish

                dish_ingredients_map[dish_name].add_ingredient_dependency(
                    ingredient, ingredient_quantity
                )

        self.dishes = set(dish_ingredients_map.values())
