import csv
import os


class StorageManager:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load(self) -> list[dict]:
        if not os.path.exists(self.file_path):
            return []

        try:
            with open(self.file_path, newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                return list(reader)
        except FileNotFoundError as e:
            print(e)
            return []

    def save(self, data: list[dict]) -> None:
        try:
            with open(self.file_path, "w", newline="", encoding="utf-8") as file:
                fields = ["id", "date", "description", "amount"]
                writer = csv.DictWriter(file, fieldnames=fields)
                writer.writeheader()
                writer.writerows(data)
        except FileNotFoundError as e:
            print(e)
