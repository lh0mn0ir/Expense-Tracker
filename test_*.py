import os
from storage import StorageManager
from manager import ExpenseManager
from expense import Expense


def test_add_expense(tmp_path):
    file_path = tmp_path/"expenses.csv"
    storage = StorageManager(file_path)
    manager = ExpenseManager(storage)

    expense = Expense(description="Transport", amount=2000)
    manager.add(expense)

    data = storage.load()

    assert len(data) == 1
    assert data[0]["description"] == "Transport"
    assert int(data[0]["amount"]) == 2000
    assert int(data[0]["id"]) == 1

def test_generate_incremented_id(tmp_path):
    file_path = tmp_path / "expenses.csv"
    storage = StorageManager(file_path)
    manager = ExpenseManager(storage)

    manager.add(Expense("Internet", 5000))
    manager.add(Expense("Nourriture", 3000))

    data = storage.load()

    assert int(data[0]["id"]) == 1
    assert int(data[1]["id"]) == 2

def test_update_expense(tmp_path):
    file_path = tmp_path / "expenses.csv"
    storage = StorageManager(file_path)
    manager = ExpenseManager(storage)

    manager.add(Expense("Taxi", 1500))

    updated = manager.update(1, {"amount": 2000})

    data = storage.load()

    assert updated is True
    assert int(data[0]["amount"]) == 2000


def test_update_non_existing_expense(tmp_path):
    file_path = tmp_path / "expenses.csv"
    storage = StorageManager(file_path)
    manager = ExpenseManager(storage)

    result = manager.update(99, {"amount": 1000})

    assert result is False
