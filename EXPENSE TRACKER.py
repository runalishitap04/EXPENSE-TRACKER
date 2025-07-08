import json
import os

# File to store expenses
FILENAME = "expenses.json"

# Load expenses from file if it exists
def load_expenses():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return []

# Save expenses to file
def save_expenses(expenses):
    with open(FILENAME, "w") as file:
        json.dump(expenses, file, indent=4)

# Add a new expense
def add_expense(expenses):
    category = input("Enter category (e.g., Food, Transport): ")
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    expense = {"category": category, "amount": amount}
    expenses.append(expense)
    print("Expense added!")

# View all expenses
def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return
    print("\nAll Expenses:")
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp['category']} - ${exp['amount']:.2f}")
    print()

# View total expense
def total_expense(expenses):
    total = sum(exp["amount"] for exp in expenses)
    print(f"Total Expenses: ${total:.2f}\n")

# Main program loop
def main():
    expenses = load_expenses()

    while True:
        print("=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_expense(expenses)
            save_expenses(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            total_expense(expenses)
        elif choice == "4":
            save_expenses(expenses)
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
