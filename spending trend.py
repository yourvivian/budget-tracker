import matplotlib.pyplot as plt
import pandas as pd

def get_total_spending(year, month):
    # read csv file into pandas dataframe
    df = pd.read_csv('budget.csv')
    
    # filter the dataframe to only include the specified year and month
    filtered_df = df[df['Date'] == f"{month} {year}"]
    
    # calculate the total amount spent in each category
    tuition_spending = filtered_df['Tuition'].sum()
    health_spending = filtered_df['Health'].sum()
    grocery_spending = filtered_df['Grocery'].sum()
    entertainment_spending = filtered_df['Entertainment'].sum()
    
    # return a dictionary of the total spending in each category
    return {'Tuition': tuition_spending, 'Health': health_spending, 'Grocery': grocery_spending, 'Entertainment': entertainment_spending}

class Budget:
    def __init__(self, income, expenses):
        if not isinstance(income, int):
            raise TypeError("Income must be an integer.")
        if not isinstance(expenses, dict):
            raise TypeError("Expenses must be a dictionary.")
        self.income = income
        self.expenses = expenses
        self.savings = income - sum(expenses.values())
    
    def calculate_total_expenses(self):
        return sum(self.expenses.values())
    
    def calculate_total_savings(self):
        return self.savings
    
    def calculate_expense_percentages(self):
        percentages = {}
        total_expenses = self.calculate_total_expenses()
        for category, amount in self.expenses.items():
            percentages[category] = amount / total_expenses * 100
        return percentages
    
    def calculate_leftover_money(self):
        return self.income - self.calculate_total_expenses()
    
    def visualize_spending_trends(self):
        expenses = list(self.expenses.values())
        categories = list(self.expenses.keys())
        plt.pie(expenses, labels=categories, autopct='%1.1f%%')
        plt.title('Spending Trends')
        plt.show()
        
        # plot a pie chart for income and savings
        income_savings = [self.income, self.savings]
        categories = ['Income', 'Savings']
        plt.pie(income_savings, labels=categories, autopct='%1.1f%%')
        plt.title('Income and Savings')
        plt.show()

    
    def generate_budget_report(self):
        total_expenses = self.calculate_total_expenses()
        total_savings = self.calculate_total_savings()
        expense_percentages = self.calculate_expense_percentages()
        leftover_money = self.calculate_leftover_money()
        report = f"Budget Report\n\nTotal Income: {self.income}\nTotal Expenses: {total_expenses}\nTotal Savings: {total_savings}\n\nExpense Percentages:"
        for category, percentage in expense_percentages.items():
            report += f"\n{category}: {percentage:.2f}%"
        report += f"\n\nLeftover Money: {leftover_money}"
        return report

monthly_total_spending_per_category = get_total_spending(2023, 'March')
print(monthly_total_spending_per_category)

my_budget = Budget(5000, monthly_total_spending_per_category)

my_budget.visualize_spending_trends()

budget_report = my_budget.generate_budget_report()
print(budget_report)
