from src.models.dish import Dish
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    pizza = "pizza"
    feijoada = "feijoada"

    dish_feijoada = Dish(feijoada, 22.00)
    dish_pizza_sea = Dish(pizza, 32.90)
    dish_pizza = Dish(pizza, 32.90)

    assert dish_pizza_sea.name == pizza
    assert repr(dish_pizza_sea) == f"Dish('{pizza}', R${32.90:.2f})"

    assert dish_pizza_sea == dish_pizza
    assert dish_pizza_sea != dish_feijoada

    assert hash(dish_pizza_sea) == hash(dish_pizza)
    assert hash(dish_pizza_sea) != hash(dish_feijoada)

    with pytest.raises(ValueError):
        Dish(pizza, 0)

    with pytest.raises(TypeError):
        Dish(pizza, "trinta e dois e noventa")

    ingredient_octopus = Ingredient("polvo")
    ingredient_shrimp = Ingredient("camarão")

    dish_pizza_sea.add_ingredient_dependency(ingredient_octopus, 19)
    dish_pizza_sea.add_ingredient_dependency(ingredient_shrimp, 35)

    assert dish_pizza_sea.get_ingredients() == {
        ingredient_octopus,
        ingredient_shrimp,
    }

    assert dish_pizza_sea.get_restrictions() == {
        Restriction.ANIMAL_MEAT,
        Restriction.SEAFOOD,
        Restriction.ANIMAL_DERIVED,
    }


if __name__ == "__main__":
    test_dish()
