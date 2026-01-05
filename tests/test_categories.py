import pytest
from app.categories import CategoryManager


def test_categories():
    c = CategoryManager()
    c.add_category("Food")
    c.add_category("Salary")
    c.add_category("food")  # duplicates ignored
    assert c.list_categories() == ["food", "salary"]

    c.remove_category("Food")
    assert c.list_categories() == ["salary"]

    with pytest.raises(ValueError):
        c.add_category("")
