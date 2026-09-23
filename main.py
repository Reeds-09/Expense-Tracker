# main.py
import expense_manager

def main():
    while True:
        print("=== Monthly Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == "1":
            expense_manager.add_new_expense()
        elif choice == "2":
            expense_manager.view_all_expenses()
        elif choice == "3":
            expense_manager.delete_expense()
        elif choice == "4":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    main()