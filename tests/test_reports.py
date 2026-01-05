from app.finance import Finance
from app.reports import generate_summary


def test_generate_summary():
    f = Finance()
    f.add_income(100, "Salary")
    f.add_expense(30, "Food")
    summary = generate_summary(f)
    assert "Total Income: 100" in summary
    assert "Total Expense: 30" in summary
    assert "Balance: 70" in summary
