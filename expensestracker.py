import os

FILENAME = "expenses.txt"

def add_expense():
    amount = input("Enter expense amount: ")
    category = input("Enter category (Food/Travel/Other): ")
    with open(FILENAME, "a") as f:
        f.write(f"{amount},{category}\n")
    print("Expense added successfully!\n")

def view_expenses():
    if not os.path.exists(FILENAME):
        print("No expenses found!\n")
        return
    print("\nYour Expenses:")
    with open(FILENAME, "r") as f:
        lines = f.readlines()
        for line in lines:
            amount, category = line.strip().split(",")
            print(f"₹{amount} - {category}")
    print()

def total_expenses():
    if not os.path.exists(FILENAME):
        print("No expenses found!\n")
        return
    total = 0
    with open(FILENAME, "r") as f:
        lines = f.readlines()
        for line in lines:
            amount, _ = line.strip().split(",")
            total += float(amount)
    print(f"Total Expenses: ₹{total}\n")

def menu():
    while True:
        print("📌 Expense Tracker Menu")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total Expenses")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Try again.\n")

menu()