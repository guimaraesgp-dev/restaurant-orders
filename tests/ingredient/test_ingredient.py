from src.models.ingredient import Ingredient, Restriction


def test_ingredient():
    meat = Ingredient("carne")
    assert meat.name == "carne"
    assert meat.restrictions == {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
    }
    assert repr(meat) == "Ingredient('carne')"

    egg = Ingredient("ovo")
    assert meat != egg
    assert meat == meat

    assert hash(meat) == hash("carne")
    assert hash(meat) != hash("ovo")


if __name__ == "__main__":
    test_ingredient()
