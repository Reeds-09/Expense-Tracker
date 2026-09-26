# file_handler.py
import os

DATA_FILE = "expenses.txt"

def read_expenses():
    """Reads all lines from the expense file using basic if-else."""
    expenses = []
    
   
    if os.path.exists(DATA_FILE):
        file = open(DATA_FILE, "r")
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 2:
                expenses.append({"name": parts[0], "amount": parts[1]})
        file.close()
        
    return expenses

def write_expense(name, amount):
    """Appends a single expense to the file."""
    file = open(DATA_FILE, "a")
    file.write(name + "," + amount + "\n")
    file.close()

def save_all_expenses(expenses):
    """Overwrites the file with updated expenses after a deletion."""
    file = open(DATA_FILE, "w")
    for exp in expenses:
        file.write(exp["name"] + "," + exp["amount"] + "\n")
    file.close()