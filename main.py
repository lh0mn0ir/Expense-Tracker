import argparse

from storage import StorageManager
from manager import ExpenseManager
from expense import Expense
from datetime import datetime

# Initialisation du stockage et manager
storage = StorageManager("expenses.csv")
manager = ExpenseManager(storage)

# Création du parser principal
parser = argparse.ArgumentParser(description="Gestionnaire de dépenses")
subparsers = parser.add_subparsers(dest="command", required=True)

# -------------------- AJOUTER --------------------
parser_add = subparsers.add_parser("add", help="Ajouter une dépense")
parser_add.add_argument("--desc", type=str, required=True, help="Description de la dépense")
parser_add.add_argument("--amount", type=float, required=True, help="Montant de la dépense")
parser_add.add_argument("--date", type=str, help="Date (YYYY-MM-DD), optionnel")

# -------------------- MODIFIER --------------------
parser_update = subparsers.add_parser("update", help="Modifier une dépense")
parser_update.add_argument("--id", type=int, required=True, help="ID de la dépense")
parser_update.add_argument("--desc", type=str, help="Nouvelle description")
parser_update.add_argument("--amount", type=float, help="Nouveau montant")
parser_update.add_argument("--date", type=str, help="Nouvelle date (YYYY-MM-DD)")

# -------------------- SUPPRIMER --------------------
parser_delete = subparsers.add_parser("delete", help="Supprimer une dépense")
parser_delete.add_argument("--id", type=int, required=True, help="ID de la dépense à supprimer")

# -------------------- AFFICHER --------------------
parser_display = subparsers.add_parser("list", help="Afficher toutes les dépenses")
parser_display.add_argument("--sort_by", type=str, choices=["date", "amount"], default="date", help="Trier par date ou montant")
parser_display.add_argument("--desc", action="store_true", help="Trier en ordre décroissant")

# -------------------- SOMMAIRE --------------------
parser_summary = subparsers.add_parser("summary", help="Afficher le total des dépenses")
parser_summary.add_argument("--month", type=str, help="Filtrer par mois (YYYY-MM)")

# -------------------- PARSE ARGS --------------------
args = parser.parse_args()

# -------------------- LOGIQUE DES COMMANDES --------------------
if args.command == "add":
    date_obj = datetime.strptime(args.date, "%Y-%m-%d").date() if args.date else None
    expense = Expense(description=args.desc, amount=args.amount, date_=date_obj)
    manager.add(expense)
    print(f"Dépense ajoutée avec succès : {expense.description}, {expense.amount}€")

elif args.command == "update":
    existing = manager.get_by_id(args.id)
    if not existing:
        print("ID introuvable")
    else:
        # Mise à jour partielle (PATCH)
        if args.desc is not None:
            existing.description = args.desc

        if args.amount is not None:
            existing.amount = args.amount

        if args.date is not None:
            existing.date = datetime.strptime(args.date, "%Y-%m-%d").date()

        manager.update(existing)
        print(f"Dépense mise à jour : ID {existing.id}")


elif args.command == "delete":
    if manager.delete(args.id):
        print(f"Dépense ID {args.id} supprimée")
    else:
        print("ID introuvable")

elif args.command == "list":
    expenses = manager.display_all(sort_by=args.sort_by, reverse=args.desc)
    import tabulate

    headers = ("ID", "Date", "Description", "Amount")
    table = [
        [e.id, e.date, e.description, e.amount]
        for e in expenses
    ]
    print(tabulate.tabulate(table, headers, tablefmt="grid"))


elif args.command == "summary":
    total = manager.summary(month=args.month)
    if args.month:
        print(f"Total dépenses pour {args.month} : {total}€")
    else:
        print(f"Total général des dépenses : {total}€")