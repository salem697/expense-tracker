from datetime import date
import json
expenses = []

def save_expenses():
    with open("expenses.json", "w")as file:
        json.dump(expenses, file, indent=4)
    print("expenses saved successfully!")
def load_expenses():
    global expenses
    try:
        with open("expenses.json", "r")as file:
            loaded_data = json.load(file)
        if isinstance(loaded_data, list):
            expenses =loaded_data
        else:
            print("Invalid file format. Starting fresh!")
            expenses = []
        print("Expenses loaded sucessfully")
    except FileNotFoundError:
        print("No previous expenses found. Starting fresh!")
    except json.JSONDecodeError:
        print("The expense file is corrupted!")
        expenses = []
def add_expense():
    try:
     expense_amount = float(input("Enter the expense amount:"))
     expense_category = input("Enter the expense category:")
     expense_date = date.today().isoformat()
     if expense_amount <= 0:
         print("Amount must be greater than zero!")
         return
     if not expense_category.strip():
         print("Category cannot be empty!")
         return
     expenses.append({
        "Amount": expense_amount,
        "Category": expense_category,
        "Date": expense_date
     })

     save_expenses()
     print("Expense added successfully!")
    except ValueError:
        print("Invalid amount! Please enter a number.")

def view_expenses():
    if not expenses:
        print("No expenses recorded yet!")
        return
    for expense in expenses:
        print("Amount:", expense["Amount"])
        print("Category:", expense["Category"])
        print("Date:", expense.get("Date", "Unknown"))
def calculate_total():
     if  not expenses:
        print("No expenses recorded yet!")
        return
     total = 0
     for expense in expenses:
        print( expense["Category"], expense["Amount"], expense.get("Date", "Unknown"))
        total += expense["Amount"]
     print("Total expenses:", total)
def monthly_report():
    month = input("Enter the month (YYYY-MM):")

    total = 0
    found = False
    for expense in expenses:
        if expense.get("Date", "").startswith(month):
            found = True
            print(
                expense["Category"],
                expense["Amount"],
                expense.get("Date", "Unknown")
            )
            total += expense["Amount"]
    if found:
        print("Total expenses for", month, ":", total)
    else:
        print("No expenses found for this month!")
def category_report():
    if not expenses:
        print("No expenses recorded yet!")
        return
    category_totals ={}
    for expense in expenses:
        category = expense["Category"].strip().title()
        amount = expense["Amount"]
        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount
    print("\nEXPENSE REPORT BY CATEGORY")
    for category, total in category_totals.items():
        print(category, ":", total)
def search_expense():
    expense_category = input("Enter the category to search:")
    found = False
    for expense in expenses:
        if expense["Category"].lower() == expense_category.lower():
            found = True
            print("Expenses found:")
            print(expense["Category"], "-", expense["Amount"],  expense.get("Date", "Unknown"))
    if not found:
            print("No expenses found!")
def delete_expense():
    if not expenses:
        print("No expenses recorded yet!")
        return
    for index, expense in enumerate(expenses, start=1):
        print(index, expense["Category"], expense["Amount"], expense.get("Date", "Unknown"))
    try:
        choice = int(input("Enter expense number to delete:"))
        if 1 <= choice <= len(expenses):
            expenses.pop(choice - 1)
            save_expenses()
            print("Expense deleted successfully")
        else:
         print("Invalid expense number!")
    except ValueError:
        print("Invalid input! Please enter a number.")
load_expenses()      
while True:
    print("EXPENSE TRACKER")
    print("1. Add an expense")
    print("2. View all expenses")
    print("3. Calculate total expenses")
    print("4. Search expenses by category")
    print("5. Delete an expense")
    print("6. Monthly expense report")
    print("7. Expense report by category")
    print("8. Exit")

    choice = input("Enter your choice:")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        calculate_total()
    elif choice == "4":
        search_expense()
    elif choice == "5":
        delete_expense()

    elif choice ==  "6":
        monthly_report()
    elif choice == "7":
        category_report()
    elif choice == "8":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! please try again")
