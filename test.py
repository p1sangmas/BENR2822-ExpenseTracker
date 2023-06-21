class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def delete_expense(self, expense):
        self.expenses.remove(expense)

    def display_expenses(self):
        for expense in self.expenses:
            print(expense)

    def generate_report(self):
        total_expenses = sum(expense.amount for expense in self.expenses)
        print("Total Expenses: $", total_expenses)


class Expense:
    def __init__(self, name, amount, category):
        self.name = name
        self.amount = amount
        self.category = category

    def __str__(self):
        return f"Name: {self.name}\nAmount: ${self.amount}\nCategory: {self.category}\n"


def create_account():
    username = input("Enter username: ")
    password = input("Enter password: ")
    return User(username, password)


def login(users):
    username = input("Enter username: ")
    password = input("Enter password: ")

    for user in users:
        if user.username == username and user.password == password:
            return user

    return None


def read_expenses(user):
    filename = f"{user.username}_expenses.txt"
    try:
        with open(filename, "r") as file:
            for line in file:
                name, amount, category = line.strip().split(",")
                expense = Expense(name, float(amount), category)
                user.add_expense(expense)
    except FileNotFoundError:
        print("File does not exist!")


def write_expenses(user):
    filename = f"{user.username}_expenses.txt"
    with open(filename, "w") as file:
        for expense in user.expenses:
            file.write(f"{expense.name},{expense.amount},{expense.category}\n")


def display_menu():
    print("Expense Tracker Menu:")
    print("1. Add Expense")
    print("2. Delete Expense")
    print("3. Display Expenses")
    print("4. Generate Report")
    print("5. Exit")


def main():
    users = []

    while True:
        print("Expense Tracker")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            user = create_account()
            users.append(user)
            print("Account created successfully!")
            print("---------------------------")
        elif choice == "2":
            user = login(users)
            if user:
                print("Login successful!")
                read_expenses(user)
                while True:
                    display_menu()
                    choice = input("Enter your choice: ")

                    if choice == "1":
                        name = input("Enter expense name: ")
                        amount = float(input("Enter expense amount: "))
                        category = input("Enter expense category: ")
                        expense = Expense(name, amount, category)
                        user.add_expense(expense)
                        print("Expense added successfully!")
                        print("---------------------------")
                    elif choice == "2":
                        print("Your Expenses:")
                        user.display_expenses()
                        expense_index = int(input("Enter the index of the expense to delete: "))
                        if 0 <= expense_index < len(user.expenses):
                            expense = user.expenses[expense_index]
                            user.delete_expense(expense)
                            print("Expense deleted successfully!")
                        else:
                            print("Invalid expense index!")
                        print("---------------------------")
                    elif choice == "3":
                        print("Your Expenses:")
                        user.display_expenses()
                        print("---------------------------")
                    elif choice == "4":
                        print("Expense Report:")
                        user.generate_report()
                        print("---------------------------")
                    elif choice == "5":
                        write_expenses(user)
                        print("Expenses saved to file.")
                        break
                    else:
                        print("Invalid choice!")
            else:
                print("Invalid username or password!")
        elif choice == "3":
            break
        else:
            print("Invalid choice!")
        print()


if __name__ == "__main__":
    main()
