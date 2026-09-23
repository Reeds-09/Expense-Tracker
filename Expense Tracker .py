def add_expense():
    name = input("Enter expense name: ")
    amount = input("Enter amount: ")
    
    # Open file in append mode
    file = open("expenses.txt", "a")
    file.write(name + "," + amount + "\n")
    file.close()
    print("Added successfully!\n")

def view_expenses():
    print("\n--- Your Expenses ---")
    try:
        file = open("expenses.txt", "r")
        for line in file:
            parts = line.strip().split(",")
            print("Item:", parts[0], "| Amount:", parts[1])
        file.close()
    except:
        print("No expenses found yet.")
    print()

def main():
    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")

main()