# expense_manager.py
import file_handler

def add_new_expense():
    """Functional Module 1: Add a new expense"""
    print("\n--- Add Expense ---")
    name = input("Enter expense name: ").strip()
    amount = input("Enter amount: ").strip()
    
    if name == "":
        print("Name cannot be empty!\n")
    elif amount == "":
        print("Amount cannot be empty!\n")
    else:
        file_handler.write_expense(name, amount)
        print("Expense added successfully!\n")

def view_all_expenses():
    """Functional Module 2: View all recorded expenses"""
    print("\n--- Your Expenses ---")
    expenses = file_handler.read_expenses()
    
    if len(expenses) == 0:
        print("No expenses found yet.\n")
    else:
        index = 1
        for exp in expenses:
            print(str(index) + ". Item: " + exp['name'] + " | Amount: " + exp['amount'])
            index = index + 1
        print()

def delete_expense():
    """Functional Module 3: Delete an existing expense"""
    print("\n--- Delete Expense ---")
    expenses = file_handler.read_expenses()
    
    if len(expenses) == 0:
        print("No expenses found to delete.\n")
    else:
        index = 1
        for exp in expenses:
            print(str(index) + ". Item: " + exp['name'] + " | Amount: " + exp['amount'])
            index = index + 1
            
        choice = input("Enter the number of the expense to delete: ").strip()
        
        # Basic check to see if input is a digit before converting
        if choice.isdigit():
            idx = int(choice) - 1
            if idx >= 0 and idx < len(expenses):
                removed = expenses.pop(idx)
                file_handler.save_all_expenses(expenses)
                print("Deleted successfully!\n")
            else:
                print("Invalid expense number.\n")
        else:
            print("Please enter a valid number.\n")