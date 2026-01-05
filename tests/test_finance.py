import pytest
from app.finance import Finance


def test_finance():
    f = Finance()
    f.add_income(100, "Salary")
    f.add_expense(40, "Food")
    f.add_expense(10, "Transport")

    assert f.total_income() == 100
    assert f.total_expense() == 50
    assert f.balance() == 50

    with pytest.raises(ValueError):
        f.add_income(-10, "Bonus")
    with pytest.raises(ValueError):
        f.add_expense(-20, "Food")
