# Expense Tracker

The Expense Tracker is a Python-based application that allows users to manage their expenses. Users can create accounts, log in, add expenses, delete expenses, view their expenses, and generate a report of their total expenses. The application also saves and loads user expenses from text files.

## Features

- **User Account Management**: Create accounts and log in securely.
- **Expense Management**: Add, delete, and view expenses.
- **Expense Categories**: Categorize expenses for better organization.
- **Expense Report**: Generate a report of total expenses.
- **File Persistence**: Save and load expenses to/from text files.

## File Structure

```
.
├── espenseTracker.py   # Main Python script for the application
├── sepul_expenses.txt  # Example expense data file
├── README.md           # Documentation file
```

## How to Run the Application

1. Ensure you have Python installed on your system (Python 3.6 or later is recommended).
2. Clone or download this repository to your local machine.
3. Open a terminal and navigate to the directory containing the `espenseTracker.py` file.
4. Run the application using the following command:

   ```bash
   python espenseTracker.py
   ```

## Usage

### Main Menu

1. **Create Account**: Create a new user account by entering a username and password.
2. **Login**: Log in to an existing account using your username and password.
3. **Exit**: Exit the application.

### Expense Tracker Menu (After Login)

1. **Add Expense**: Add a new expense by providing the name, amount, and category.
2. **Delete Expense**: Delete an existing expense by selecting its index from the list.
3. **Display Expenses**: View all your expenses in a formatted list.
4. **Generate Report**: View the total amount of all your expenses.
5. **Back to Home Screen**: Save your expenses to a file and return to the main menu.

### File Persistence

- Expenses are saved to a file named `<username>_expenses.txt` in the same directory as the script.
- When you log in, the application automatically loads your expenses from this file if it exists.

## Example

### Example Expense File (`sepul_expenses.txt`)

```txt
balls,4.0,sports
cabbage,5.0,veges
cd,45.0,games
water,1.3,foods
```

### Sample Output

#### Main Menu
```
Main Menu:
1. Create Account
2. Login
3. Exit
```

#### Expense Tracker Menu
```
Expense Tracker Menu:
1. Add Expense
2. Delete Expense
3. Display Expenses
4. Generate Report
5. Back to Home Screen
```

#### Expense Report
```
Total Expenses: RM 55.3
```

## Dependencies

This application does not require any external libraries. It uses Python's built-in modules.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Contributions are welcome!

## Author

Developed by Fakhrul Fauzi.
