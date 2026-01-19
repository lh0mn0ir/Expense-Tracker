from datetime import date


class Expense:
    def __init__(self, id_: int, description: str, amount: float = 0.0, expense_date=None):
        self.id = id_
        self.description = description
        self.amount = amount
        self.date = expense_date or date.today()

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "description": self.description,
            "amount": self.amount,
            "date": self.date,
        }
