from typing import List, Dict


class Finance:
    def __init__(self):
        self.incomes: List[Dict] = []
        self.expenses: List[Dict] = []

    def add_income(self, amount: float, category: str):
        if amount <= 0:
            raise ValueError("Income must be positive")
        self.incomes.append({"amount": amount, "category": category})

    def add_expense(self, amount: float, category: str):
        if amount <= 0:
            raise ValueError("Expense must be positive")
        self.expenses.append({"amount": amount, "category": category})

    def total_income(self) -> float:
        return sum(i["amount"] for i in self.incomes)

    def total_expense(self) -> float:
        return sum(e["amount"] for e in self.expenses)

    def balance(self) -> float:
        return self.total_income() - self.total_expense()
