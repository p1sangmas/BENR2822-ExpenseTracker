# import os is for checking if file exists in the system
import os

# Class User is for creating a user object
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.expenses = []

    # add_expense() is for adding an expense object to the expenses list
    def add_expense(self, expense):
        self.expenses.append(expense)

    # delete_expense() is for deleting an expense object from the expenses list
    def delete_expense(self, expense):
        self.expenses.remove(expense)

    # display_expenses() is for displaying all the expense objects in the expenses list
    def display_expenses(self):
        for expense in self.expenses:
            print(expense)

    # generate_report() is for generating a report of all the expenses in the expenses list
    def generate_report(self):
        total_expenses = sum(expense.amount for expense in self.expenses)
        print("\nTotal Expenses: RM", total_expenses)

# Class Expense is for creating an expense object
class Expense:
    def __init__(self, name, amount, category):
        self.name = name
        self.amount = amount
        self.category = category

    def __str__(self):
        return f"Name: {self.name}\nAmount: RM{self.amount}\nCategory: {self.category}\n"

# create_account() is for creating a user object
def create_account():
    username = input("Enter username: ")
    password = input("Enter password: ")
    return User(username, password)

# login() is for logging in a user
def login(users):
    username = input("Enter username: ")
    password = input("Enter password: ")

    # for loop is for checking if the username and password is in the users list
    for user in users:
        if user.username == username and user.password == password:
            return user

    return None

# read_expenses() is for reading the expenses from the file
def read_expenses(user):
    filename = f"{user.username}_expenses.txt"

    #os.path.isfile() is for checking if the file exists in the system
    if os.path.isfile(filename):
        with open(filename, "r") as file:
            for line in file:
                # line.strip().split(",") is for splitting the line into 3 parts
                name, amount, category = line.strip().split(",")
                expense = Expense(name, float(amount), category)
                user.add_expense(expense)
    else:
        print("\nFile does not exist!\n")

# write_expenses() is for writing the expenses to the file
def write_expenses(user):
    filename = f"{user.username}_expenses.txt"
    with open(filename, "w") as file:
        for expense in user.expenses:
            file.write(f"{expense.name},{expense.amount},{expense.category}\n")

# display_menu() is for displaying the menu
def display_menu():
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. Delete Expense")
    print("3. Display Expenses")
    print("4. Generate Report")
    print("5. Back to Home Screen")

# main() is for running the program
def main():

    # users list is for storing all the user objects
    users = []

    while True:
        print("Main Menu:")
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
                print("Login successful!\n")
                read_expenses(user)
                while True:
                    display_menu()
                    choice = input("Enter your choice: ")

                    if choice == "1":
                        name = input("Enter expense name: ")
                        amount = float(input("Enter expense amount (RM): "))
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
                        print("\nYour Expenses:")
                        user.display_expenses()
                        print("---------------------------")
                    elif choice == "4":
                        print("\nTotal Expense Report:")
                        user.generate_report()
                        print("---------------------------")
                    elif choice == "5":
                        write_expenses(user)
                        print("\nExpenses saved to file.")
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
