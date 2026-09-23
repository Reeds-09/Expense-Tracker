# Monthly Expense Tracker

A simple, command-line-based Monthly Expense Tracker built using core Python. This application allows users to add, view, and delete daily expenses with local file storage.

---

## Features

* **Add Expense:** enter a new expense item and its price
* **View Expenses:** Display all recorded in a  numbered list.
* **Delete Expense:** Remove unwanted or incorrect expense records.
* **Data Persistence:** Automatically saves all records locally to a text file (`expenses.txt`).



## Technologies Used

* **Python 3.x** (no external libraries required)



## Project Structure

The project is organized into modular files:
* `main.py`: Runs the interactive command-line menu loop.
* `expense_manager.py`: Contains the core logic for adding, viewing, and deleting expenses.
* `file_handler.py`: Handles reading from and writing to the local data file.



## How to Install and Run

1. **Clone or Download** this repository to your local machine.
2. Open your terminal or command prompt inside the project folder.
3. Run the application using the following command:
   ```bash
   python main.py


**How to Test**
Start the application by running python main.py.

Choose option 1 to add a test expense (e.g., Name: Coffee, Amount: 50).

Choose option 2 to verify that the expense appears in the list.

Choose option 3 to test deleting the expense.

Choose option 4 to exit the application.


**Screenshot**

<img width="1656" height="416" alt="Screenshot 2026-09-23 200546" src="https://github.com/user-attachments/assets/b4058beb-13ef-47c9-9e5a-d1ef6cf66986" />


