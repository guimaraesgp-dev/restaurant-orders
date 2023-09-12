import pandas as pd
from models.dish import Dish
from models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.csv_reader = pd.read_csv(source_path).itertuples(index=False)
        self.dishes = set()

        self.load_menu_data()

    def load_menu_data(self):
        dish_dict = {}

        for row in self.csv_reader:
            name, price, ingredient, amount = row

            if name not in dish_dict:
                dish = Dish(name, price)
                dish_dict[name] = dish
                self.dishes.add(dish)

            ingredient_obj = Ingredient(ingredient)
            dish_dict[name].add_ingredient_dependency(ingredient_obj, amount)

    def __len__(self):
        return len(self.dishes)
