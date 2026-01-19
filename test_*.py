import storage

expenses = storage.StorageManager("expenses.csv").load()
expense = {"id":4, "description":"Galadiner", "amount":550.0, "date":None}
expenses.append(expense)
storage.StorageManager("expenses.csv").save(expenses)