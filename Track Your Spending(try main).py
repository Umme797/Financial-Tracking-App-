#Importing necessary libraries
from datetime import datetime  # for handling dates and times
import matplotlib.pyplot as plt  # for data visualization



# Define a class to represent a User
class User:



    # Initialize the user 
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.spending_limits = {}
        self.expenses = {}



    # Method to add an expense to a specific category
    def add_expense(self, category, amount):
        if amount > 0:
            if category not in self.expenses:
                self.expenses[category] = []
            expense_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.expenses[category].append({"amount": amount, "date": expense_date})
            print("Expense added successfully!")
        else:
            print("Expense must be positive")



    # Method to view all expenses for each category
    def view_expenses(self):
        for category, expense_list in self.expenses.items():
            print(f"Category: {category}")
            for expense in expense_list:
                print(f"  Amount: {expense['amount']}, Date: {expense['date']}")



    # Method to set a spending limit for a specific category
    def set_spending_limit(self, category, limit_amount):
        self.spending_limits[category] = limit_amount
        print("Spending limit set successfully!")



    # Method to check if the user has exceeded their spending limit
    def check_spending_limit(self):
        total_spending = 0
        # Calculate total spending across all categories
        for category in self.expenses:
            for expense in self.expenses[category]:
                total_spending += expense["amount"]

        # Compare with the spending limits set for each category
        for category, limit in self.spending_limits.items():
            category_spending = sum(expense["amount"] for expense in self.expenses.get(category, []))
            print(f"Spending for {category}: {category_spending:.2f}, Limit: {limit:.2f}")
            if category_spending > limit:
                print(f"You have exceeded your limit for {category}!")
            else:
                remaining = limit - category_spending
                print(f"You have {remaining:.2f} remaining in your {category} limit.")



    # Method to generate a report of expenses between two dates
    def generate_report(self, start_date, end_date):
        total_report = 0
        for category, expense_list in self.expenses.items():
            for expense in expense_list:
                expense_date = datetime.strptime(expense["date"], "%Y-%m-%d %H:%M:%S")
                if start_date <= expense_date.date() <= end_date:
                    total_report += expense["amount"]
        print(f"Total expenses from {start_date} to {end_date}: {total_report}")



    # Method to visualize spending across categories using a bar chart
    def visualize_spending(self):
        categories = list(self.expenses.keys())  
        totals = [sum(expense["amount"] for expense in self.expenses[category]) for category in categories]
        plt.bar(categories, totals)
        plt.xlabel('Category')
        plt.ylabel('Amount')
        plt.title('Spending by Category')
        plt.show()



# Function to create a new user account
def create_account():
    while True:
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        if username and password:  # Check if neither is empty
            user = User(username, password)
            print("Account created successfully!")
            return user
        else:
            print("Username and password cannot be empty. Try again.")



# Function for user login
def login(users):
    try:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        for user in users:
            if user.username == username and user.password == password:
                print("Login successful!")
                return user
        raise ValueError("Invalid username or password. Try again.")
    except ValueError as e:
        print(e)
        return None



# Main function to run the application
def main():
    users = []
    while True:
        print("1. Create Account")
        print("2. Login")
        choice = input("Choose an option: ")
        if choice == "1":
            user = create_account()
            users.append(user)
        elif choice == "2":
            user = login(users)
            if user:
                while True:
                    print("1. Add Expense")
                    print("2. View Expenses")
                    print("3. Set Spending Limit")
                    print("4. Check Spending Limit")
                    print("5. Generate Report")
                    print("6. Visualize Spending")
                    choice = input("Choose an option: ")
                    if choice == "1":
                        try:
                            category = input("Enter the category (e.g., groceries, entertainment, utilities): ")
                            amount = float(input("Enter the expense amount: "))
                            user.add_expense(category, amount)
                        except ValueError:
                            print("Invalid input. Please enter a number for the amount.")
                    elif choice == "2":
                        user.view_expenses()
                    elif choice == "3":
                        try:
                            category = input("Enter the category (e.g., groceries, entertainment, utilities): ")
                            limit_amount = float(input("Enter the spending limit: "))
                            user.set_spending_limit(category, limit_amount)
                        except ValueError:
                            print("Invalid input. Please enter a number for the spending limit.")
                    elif choice == "4":
                        user.check_spending_limit()
                    elif choice == "5":
                        try:
                            start_date_str = input("Enter the start date (YYYY-MM-DD): ")
                            end_date_str = input("Enter the end date (YYYY-MM-DD): ")
                            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
                            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
                            user.generate_report(start_date, end_date)
                        except ValueError:
                            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
                    elif choice == "6":
                        user.visualize_spending()
                    else:
                        print("Invalid option. Try again.")
        else:
            print("Invalid option. Try again.")



# Call the main function to start the program
main()
