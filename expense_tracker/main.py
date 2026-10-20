
import json
from pathlib import Path

FILE = Path(__file__).parent / "expenses.json"
expenses = []


def load_expenses():
    if FILE.exists():
        with open(FILE, "r") as file:
            return json.load(file)
    return []


def save_expenses():
    with open(FILE, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense():
    description = input("Description: ").strip()

    if not description:
        print("Description cannot be empty.")
        return

    try:
        amount = float(input("Amount in naira: "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
    except ValueError:
        print("Enter a valid amount.")
        return

    expenses.append({
        "description": description,
        "amount": amount
    })

    save_expenses()
    print("Expense added!")


def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return

    for number, expense in enumerate(expenses, 1):
        print(f"{number}. {expense['description']} - "
              f"₦{expense['amount']:.2f}")


def show_total():
    total = sum(item["amount"] for item in expenses)
    print(f"Total: ₦{total:.2f}")


def main():
    global expenses
    expenses = load_expenses()

    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Show total")
        print("q. Quit")

        choice = input("Choose an option: ").strip().lower()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_total()
        elif choice == "q":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
