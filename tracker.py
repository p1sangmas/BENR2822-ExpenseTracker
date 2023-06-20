import os
# Function to read expenses from file
def read_expenses():
    expenses = []
    if os.path.exists('expenses.txt'):
        with open('expenses.txt', 'r') as file:
            for line in file:
                expense_data = line.strip().split(',')
                expense = {
                    'id': int(expense_data[0]),
                    'description': expense_data[1],
                    'amount': float(expense_data[2]),
                    'date': expense_data[3],
                    'category': expense_data[4]
                }
                expenses.append(expense)
    else:
        print("Expenses file not found!")
    return expenses

# Function to write expenses to file
def write_expenses(expenses):
    with open('expenses.txt', 'w') as file:
        for expense in expenses:
            line = f"{expense['id']},{expense['description']},{expense['amount']},{expense['date']},{expense['category']}\n"
            file.write(line)


# Function to add an expense
def add_expense(expenses):
    description = input("Enter expense description: ")
    amount = float(input("Enter expense amount: "))
    date = input("Enter expense date (YYYY-MM-DD): ")
    category = input("Enter expense category: ")
    
    expense_id = 1 if len(expenses) == 0 else expenses[-1]['id'] + 1
    expenses.append({
        'id': expense_id,
        'description': description,
        'amount': amount,
        'date': date,
        'category': category
    })
    write_expenses(expenses)
    print("Expense added successfully!")


# Function to display expenses
def display_expenses(expenses):
    if len(expenses) == 0:
        print("No expenses found!")
        return
    print("Expense List:")
    for expense in expenses:
        print(f"ID: {expense['id']}, Description: {expense['description']}, Amount: {expense['amount']}, Date: {expense['date']}, Category: {expense['category']}")
    print()

# Function to delete an expense
def delete_expense(expenses):
    expense_id = int(input("Enter the expense ID to delete: "))
    for expense in expenses:
        if expense['id'] == expense_id:
            expenses.remove(expense)
            write_expenses(expenses)
            print("Expense deleted successfully!")
            return
    print("Expense not found!")


# Function to generate expense reports
def generate_report(expenses):
    category = input("Enter the category to generate the report (leave blank for all categories): ")
    total_expenses = 0
    filtered_expenses = []
    
    if category == "":
        filtered_expenses = expenses
    else:
        for expense in expenses:
            if expense['category'] == category:
                filtered_expenses.append(expense)
    
    if len(filtered_expenses) == 0:
        print("No expenses found for the given category!")
        return
    
    print("Expense Report:")
    for expense in filtered_expenses:
        print(f"Description: {expense['description']}, Amount: {expense['amount']}, Date: {expense['date']}")
        total_expenses += expense['amount']
    
    print(f"\nTotal expenses for category '{category}': {total_expenses}\n")

    
# Main function
def main():
    expenses = read_expenses()
    
    while True:
        print("Expense Tracker Menu:")
        print("1. Add Expense")
        print("2. Delete Expense")
        print("3. Display Expenses")
        print("4. Generate Expense Report")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            delete_expense(expenses)
        elif choice == "3":
            display_expenses(expenses)
        elif choice == "4":
            generate_report(expenses)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == '__main__':
    main()