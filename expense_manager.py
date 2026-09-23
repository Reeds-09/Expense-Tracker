# expense_manager.py
import file_handler

def add_new_expense():
    """Functional Module 1: Add a new expense"""
    print("\n--- Add Expense ---")
    name = input("Enter expense name: ").strip()
    amount = input("Enter amount: ").strip()
    
    if name == "" or amount == "":
        print("Fields cannot be empty!\n")
        return
        
    file_handler.write_expense(name, amount)
    print("Expense added successfully!\n")

def view_all_expenses():
    """Functional Module 2: View all recorded expenses"""
    print("\n--- Your Expenses ---")
    expenses = file_handler.read_expenses()
    if not expenses:
        print("No expenses found yet.\n")
        return
    
    for index, exp in enumerate(expenses, start=1):
        print(f"{index}. Item: {exp['name']} | Amount: {exp['amount']}")
    print()

def delete_expense():
    """Functional Module 3: Delete an existing expense"""
    print("\n--- Delete Expense ---")
    expenses = file_handler.read_expenses()
    if not expenses:
        print("No expenses found to delete.\n")
        return
    
    for index, exp in enumerate(expenses, start=1):
        print(f"{index}. Item: {exp['name']} | Amount: {exp['amount']}")
    
    choice = input("Enter the number of the expense to delete: ").strip()
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(expenses):
            removed = expenses.pop(idx)
            file_handler.save_all_expenses(expenses)
            print(f"Deleted '{removed['name']}' successfully!\n")
        else:
            print("Invalid expense number.\n")
    except ValueError:
        print("Please enter a valid number.\n")