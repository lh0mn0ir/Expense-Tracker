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

def test_delete_expense(tmp_path):
    file_path = tmp_path / "expenses.csv"
    storage = StorageManager(file_path)
    manager = ExpenseManager(storage)

    manager.add(Expense("Diner", 5000))
    manager.add(Expense("Brunch", 15000))

    delete = manager.delete(1)

    data = storage.load()
    assert delete is True
    assert len(data) == 1

def test_display_all_sorted_by_amount(tmp_path):
    manager = ExpenseManager(StorageManager(tmp_path / "expenses.csv"))

    manager.add(Expense("A", 3000))
    manager.add(Expense("B", 1000))
    manager.add(Expense("C", 2000))

    expenses = manager.display_all(sort_by="amount")

    amounts = [e.amount for e in expenses]

    assert amounts == [1000, 2000, 3000]

def test_summary_all(tmp_path):
    manager = ExpenseManager(StorageManager(tmp_path / "expenses.csv"))

    manager.add(Expense("A", 1000))
    manager.add(Expense("B", 2000))

    total = manager.summary()
    assert total == 3000

def test_summary_with_month(tmp_path):
    from datetime import date

    manager = ExpenseManager(StorageManager(tmp_path / "expenses.csv"))

    e1 = Expense("Jan", 1000, date_=date(2026, 1, 10))
    e2 = Expense("Feb", 2000, date_=date(2026, 2, 5))

    manager.add(e1)
    manager.add(e2)

    total = manager.summary("2026-01")

    assert total == 1000


def test_display_all_empty(tmp_path):
    file_path = tmp_path / "expenses.csv"
    storage = StorageManager(file_path)
    manager = ExpenseManager(storage)

    data = manager.display_all()

    assert data == []
