from datetime import date


class Expense:
    def __init__(
        self, description: str, amount: float, id_: int = None, date_: date = None
    ):
        self.id = id_
        self.description = description
        self.amount = amount
        self.date = date_ if date_ else date.today()
    # convertion de l'objet Epense en dictionnaire
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "date": self.date,
            "description": self.description,
            "amount": self.amount,
        }
    # convertion d'un dictionnaire en objet Expense
    @staticmethod
    def from_dict(data: dict) -> "Expense":
        return Expense(
            id_=data.get("id"),
            description=data.get("description"),
            amount=float(data.get("amount")),
            date_=data.get("date"),
        )
