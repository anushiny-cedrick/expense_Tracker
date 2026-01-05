from .finance import Finance


def generate_summary(finance: Finance) -> str:
    summary = (
        f"Total Income: {finance.total_income()}\n"
        f"Total Expense: {finance.total_expense()}\n"
        f"Balance: {finance.balance()}\n"
    )
    return summary
