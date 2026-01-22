
# Expenses Tracker

## Description

Expense Tracker est une application CLI simple pour suivre et gérer vos dépenses quotidiennes. 
Vous pouvez ajouter, modifier, supprimer et filtrer vos dépenses. 
Les dépenses sont stockées dans un fichier CSV local.

## url du projet
https://roadmap.sh/projects/expense-tracker

## Fonctionnalités

- Ajouter une dépense
- Mettre à jour une dépense (description, montant ou date)
- Supprimer une dépense
- lister toute les dépenses
- voir le total de toutes les dépenses en spécifiant ou pas le mois 

## Installation

1. Clonez le dépôt avec:
```bash
git clone https://github.com/lh0mn0ir/Expense-Tracker-.git
```
2. Assurez-vous d'avoir Python 3 installé.
3. Placez-vous dans le dossier `expense-tracker` avec:
```bash
cd expense-tracker
```

## Utilisation

Lancez le programme principal avec python :

```bash
python main.py <commande> [arguments]
```

### Commandes disponibles

- **Ajouter une dépense**
    ```bash
    python main.py add --desc <description> --amount <montant>
    # Exemple : python main.py add --desc "Vêtements" --amount 2000
    ```

- **Mettre à jour une dépense**
    ```bash
    python main.py update --id <id> --desc <Nouvelle description>  --amount <montant> --date <date>
    # Exemple : python main.py update --id 1 --amount 1000
    ```

- **Supprimer une dépense**
    ```bash
    python main.py delete --id <id>
    # Exemple : python main.py delete --id 1
    ```


- **Lister toutes les tâches**
    ```bash
    python main.py list
  # ID    Date      Description    Amount
  # 1     2026-01   "Vêtements"     2000
  # 1     2026-02   "Uber"          2000
  # 1     2026-01   "chaussures"    2000
    ```
- **Lister toutes les dépenses par mois**
    ```bash
    python main.py list --month <mois>
    ```


## Structure du projet

- `main.py` : programme principal CLI
- `expense.py` : logique métier et gestion des dépenses
- `storage.py` : gestion du stockage CSV
- `expenses.csv` : base de données locale des dépenses
- `test_*.py` : tests unitaires


## Auteur

Projet réalisé par Lhomnoir.

