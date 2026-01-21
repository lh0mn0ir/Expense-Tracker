from storage import StorageManager
from expense import Expense


class ExpenseManager:
    def __init__(self, storage: StorageManager):
        self.storage = storage
    # génération automatique de l'ID
    def _generate_id(self) -> int:
        data = self.storage.load()
        if not data:
            return 1
        return max(int(e["id"]) for e in data) + 1

    def get_by_id(self, id_: int) :
        data = self.storage.load()
        for e in data:
            if int(e.get("id")) == id_:
                return  Expense.from_dict(e)
        return False

    # ajout d'une dépense
    def add(self, expense: Expense) -> Expense:
        expenses = self.storage.load()

        expense.id = self._generate_id()
        expenses.append(expense.to_dict())

        self.storage.save(expenses)
        return expense

    # modifiction d'une dépense
    def update(self, id_: int, update_data: dict) -> bool:
        data = self.storage.load()
        for idx, expense_data in enumerate(data):
            if int(expense_data["id"]) == id_:
                for key, value in update_data.items():
                    expense_data[key] = value
                self.storage.save(data)
                return True
        return False

    # supprimer une dépense
    def delete(self, id_: int) -> bool:
        data = self.storage.load()
        for idx, expense_data in enumerate(data):
            if int(expense_data["id"]) == id_:
                data.pop(idx)
                self.storage.save(data)
                return True
        return False

    # afficher toutes les dépenses avec ou sans tri
    def display_all(self, sort_by: str = "date", reverse: bool = False) -> list[Expense]:
        data = self.storage.load()
        expenses = [
            Expense.from_dict(expense_data)
            for expense_data in data
        ]
        if sort_by == "amount":
            return sorted(expenses, key=lambda e: e.amount, reverse=reverse)

        return sorted(expenses, key=lambda e: e.date, reverse=reverse)

    # total de toutes  dépenses ou par mois
    def summary(self, month: str = None) -> float:
        expenses = self.display_all()
        if month:
            expenses = [
                expense
                for expense in expenses
                if expense.date.startswith(month)
            ]

        return sum(expense.amount for expense in expenses)


