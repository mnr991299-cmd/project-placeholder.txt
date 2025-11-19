expenses = []

def add_expense():
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")
    expenses.append({"amount": amount, "description": description})
    print("Expense added!\n")

def show_expenses():
    print("\nYour Expenses:")
    for e in expenses:
        print(f"₹{e['amount']} - {e['description']}")
    print()

def total_expenses():
    total = sum(e["amount"] for e in expenses)
    print(f"\nTotal Expenses: ₹{total}\n")

while True:
    print("1. Add Expense")
    print("2. Show Expenses")
    print("3. Total Expenses")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        show_expenses()
    elif choice == "3":
        total_expenses()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Try again.\n")