from storage import StorageManager
from expense import Expense


class ExpenseManager:
    def __init__(self, storage: StorageManager):
        self.storage = storage

    def _generate_id(self) -> int:
        expenses = self.storage.load()
        if not expenses:
            return 1
        return max(expense.get("id", 0) for expense in expenses) + 1

    def add(self, expense: Expense):
        expenses = self.storage.load()
        expenses.append(expense.to_dict())
        self.storage.save(expenses)

