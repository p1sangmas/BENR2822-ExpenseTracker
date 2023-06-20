import os

class Expense:
    def __init__(self, expense_id, description, amount, date, category):
        self.id = expense_id
        self.description = description
        self.amount = amount
        self.date = date
        self.category = category

    def __str__(self):
        return f"ID: {self.id}, Description: {self.description}, Amount: {self.amount}, Date: {self.date}, Category: {self.category}"

class ExpenseTracker:
    def __init__(self):
        self.expenses = self.read_expenses()

    # Function to read expenses from file
    def read_expenses(self):
        expenses = []
        if os.path.exists('expenses.txt'):
            with open('expenses.txt', 'r') as file:
                for line in file:
                    expense_data = line.strip().split(',')
                    expense = Expense(int(expense_data[0]), expense_data[1], float(expense_data[2]), expense_data[3], expense_data[4])
                    expenses.append(expense)
        else:
            print("File does not exist!")
        return expenses
    
    # Function to write expenses to file
    def write_expenses(self):
        with open('expenses.txt', 'w') as file:
            for expense in self.expenses:
                line = f"{expense.id},{expense.description},{expense.amount},{expense.date},{expense.category}\n"
                file.write(line)

    # Function to add an expense
    def add_expense(self):
        description = input("Enter expense description: ")
        amount = float(input("Enter expense amount: "))
        date = input("Enter expense date (YYYY-MM-DD): ")
        category = input("Enter expense category: ")

        expense_id = 1 if len(self.expenses) == 0 else self.expenses[-1].id + 1
        expense = Expense(expense_id, description, amount, date, category)
        self.expenses.append(expense)
        self.write_expenses()
        print("Expense added successfully!")

    # Function to delete an expense
    def delete_expense(self):
        expense_id = int(input("Enter the expense ID to delete: "))
        for expense in self.expenses:
            if expense.id == expense_id:
                self.expenses.remove(expense)
                self.write_expenses()
                print("Expense deleted successfully!")
                return
        print("Expense not found!")

    # Function to display expenses
    def display_expenses(self):
        if len(self.expenses) == 0:
            print("No expenses found!")
            return
        print("Expense List:")
        for expense in self.expenses:
            print(expense)
        print()

    # Function to generate expense reports
    def generate_report(self):
        category = input("Enter the category to generate the report (leave blank for all categories): ")
        total_expenses = 0
        filtered_expenses = []

        if category == "":
            filtered_expenses = self.expenses
        else:
            for expense in self.expenses:
                if expense.category == category:
                    filtered_expenses.append(expense)

        if len(filtered_expenses) == 0:
            print("No expenses found for the given category!")
            return

        print("Expense Report:")
        for expense in filtered_expenses:
            print(expense)
            total_expenses += expense.amount

        print(f"\nTotal expenses for category '{category}': {total_expenses}\n")

class EnhancedExpenseTracker(ExpenseTracker):
    def __init__(self):
        ExpenseTracker.__init__(self)

    def add_expense(self):
        ExpenseTracker.add_expense(self)
        print("Expense added in the enhanced tracker!")

# Main function
def main():
    tracker = EnhancedExpenseTracker()

    while True:
        print("Expense Tracker Menu:")
        print("1. Add Expense")
        print("2. Delete Expense")
        print("3. Display Expenses")
        print("4. Generate Expense Report")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            tracker.add_expense()
        elif choice == "2":
            tracker.delete_expense()
        elif choice == "3":
            tracker.display_expenses()
        elif choice == "4":
            tracker.generate_report()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == '__main__':
    main()
