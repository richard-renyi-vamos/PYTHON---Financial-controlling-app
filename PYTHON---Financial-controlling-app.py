import pandas as pd
import matplotlib.pyplot as plt

class FinancialController:
    def __init__(self):
        self.budget = 0
        self.expenses = pd.DataFrame(columns=['Date', 'Category', 'Amount'])
    
    def set_budget(self, amount):
        self.budget = amount
        print(f"Budget set to: {self.budget} HUF")
    
    def add_expense(self, date, category, amount):
        new_expense = pd.DataFrame({'Date': [date], 'Category': [category], 'Amount': [amount]})
        self.expenses = pd.concat([self.expenses, new_expense], ignore_index=True)
        print(f"Expense added: {amount} HUF for {category} on {date}")
    
    def get_total_expenses(self):
        return self.expenses['Amount'].sum()
    
    def generate_report(self):
        total_expenses = self.get_total_expenses()
        remaining_budget = self.budget - total_expenses
        
        print("\nFinancial Report:")
        print("-------------------")
        print(f"Budget: {self.budget} HUF")
        print(f"Total Expenses: {total_expenses} HUF")
        print(f"Remaining Budget: {remaining_budget} HUF")
        
        if remaining_budget < 0:
            print("Warning: You have exceeded your budget!")
    
    def visualize_expenses(self):
        if self.expenses.empty:
            print("No expenses to show.")
            return
        
        category_totals = self.expenses.groupby('Category')['Amount'].sum()
        
        plt.figure(figsize=(8, 5))
        category_totals.plot(kind='bar', color='skyblue', edgecolor='black')
        plt.title('Expenses by Category')
        plt.xlabel('Category')
        plt.ylabel('Amount (HUF)')
        plt.xticks(rotation=45)
        plt.show()

# Example usage
controller = FinancialController()
controller.set_budget(500000)
controller.add_expense('2025-03-01', 'Rent', 200000)
controller.add_expense('2025-03-05', 'Groceries', 50000)
controller.add_expense('2025-03-10', 'Transport', 30000)
controller.generate_report()
controller.visualize_expenses()
