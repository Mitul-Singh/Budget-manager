class BudgetManager:
    def __init__(self, budget_limit):
        # Constructor method to initialize the budget limit and an empty list for expenses
        self.budget_limit = budget_limit
        self.expenses = []

    def add_expense(self, description, amount):
        # Method to add a new expense with description and amount
        self.expenses.append((description, amount))

    def total_expenses(self):
        # Method to calculate the total of all expenses
        return sum(amount for _, amount in self.expenses)

    def view_expenses(self):
        # Method to print all recorded expenses
        if not self.expenses:
            # Check if there are no expenses recorded
            print("No expenses recorded yet.")
        else:
            # Print the list of expenses
            print("List of Expenses:")
            for i, (desc, amount) in enumerate(self.expenses, start=1):
                # Print each expense with its description and amount
                print(f"{i}. {desc}: ${amount}")

    def remaining_budget(self):
        # Method to calculate the remaining budget
        return self.budget_limit - self.total_expenses()

    def check_budget(self):
        # Method to check if the total expenses exceed the budget limit
        if self.total_expenses() > self.budget_limit:
            print("Budget limit exceeded!")

# Example usage of the BudgetManager class
def main():
    # Main function to interact with the user
    budget_limit = float(input("Enter your budget limit: $"))
    # Create an instance of BudgetManager with the provided budget limit
    manager = BudgetManager(budget_limit)

    while True:
        # Display the menu options to the user
        print("\n===== Budget Manager Menu =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Remaining Budget")
        print("5. Check Budget Limit")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            # Option to add a new expense
            desc = input("Enter expense description: ")
            amount = float(input("Enter amount spent: $"))
            # Add the expense to the manager
            manager.add_expense(desc, amount)
            print("Expense added successfully!")

        elif choice == "2":
            # Option to view all expenses
            manager.view_expenses()

        elif choice == "3":
            # Option to view the total expenses
            total = manager.total_expenses()
            print(f"Total expenses: ${total}")

        elif choice == "4":
            # Option to view the remaining budget
            remaining = manager.remaining_budget()
            print(f"Remaining budget: ${remaining}")

        elif choice == "5":
            # Option to check if the budget limit has been exceeded
            manager.check_budget()

        elif choice == "6":
            # Option to exit the program
            print("Exiting...")
            break

        else:
            # Handle invalid menu choices
            print("Invalid choice. Please enter a number from 1 to 6.")

# Entry point of the script
if __name__ == "__main__":
    main()
