from storage import StorageManager
from expense import Expense


class ExpenseManager:
    def __init__(self, storage: StorageManager):
        self.storage = storage

    def _generate_id(self) -> int:
        data = self.storage.load()
        if not data:
            return 1
        return max(int(expense["id"]) for expense in data) + 1

    def add(self, expense: Expense) -> Expense:
        expenses = self.storage.load()

        expense.id = self._generate_id()
        expenses.append(expense.to_dict())

        self.storage.save(expenses)
        return expense

    def update(self, id_: int, update_data: dict) -> bool:
        expenses = self.storage.load()

        for expense in expenses:
            if int(expense["id"]) == id_:
                expense["description"] = update_data.get(
                    "description", expense["description"]
                )
                expense["amount"] = update_data.get("amount", expense["amount"])
                expense["date"] = update_data.get("date", expense["date"])

                self.storage.save(expenses)
                return True

        return False


    def delete(self, _id: int) -> bool:
        data = self.storage.load()

        for idx, expense in enumerate(data):
            if int(expense["id"]) == _id:
                data.pop(idx)
                self.storage.save(data)
                return True

        return False

    def display_all(self, sort_by: str = "date", reverse: bool = False) -> list:
        data = self.storage.load()

        # tri par montant
        if sort_by == "amount":
            return sorted(
                data,
                key=lambda expense: float(expense["amount"]),
                reverse=reverse
            )

        # tri par date (par défaut)
        return sorted(
            data,
            key=lambda expense: expense["date"],
            reverse=reverse
        )

    def summary(self, month: str = None) -> float:
        data = self.storage.load()

        if not data:
            return 0.0

        if month:
            data = [
                expense
                for expense in data
                if expense["date"].startswith(month)
            ]

        return sum(float(expense["amount"]) for expense in data)

