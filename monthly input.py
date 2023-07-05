import os
import pandas as pd
from datetime import datetime

# get current month and year
now = datetime.now()
month = now.strftime("%B")
year = now.year

# define categories
categories = ['Tuition', 'Health', 'Grocery', 'Entertainment']

# create empty budget dictionary with categories as keys and empty lists as values
budget_dict = {}
for category in categories:
    budget_dict[category] = []

# check if csv file exists, otherwise create it
if not os.path.isfile('budget.csv'):
    df = pd.DataFrame(columns=['Date'] + categories)
    df.to_csv('budget.csv', index=False)

# read csv file into pandas dataframe
df = pd.read_csv('budget.csv')
df = df.rename(columns={'category': 'Date', 'Spent': categories[0]})

# prompt user to input expenses for each category
for category in categories:
    while True:
        try:
            expense = float(input(f"New amount spent on {category} this month: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # append the expense to the corresponding category in the budget dictionary
    budget_dict[category].append(expense)

# append the current month's budget to the pandas dataframe
date_exists = False
for index, row in df.iterrows():
    if row['Date'] == f'{month} {year}':
        date_exists = True
        for category in categories:
            row[category] += budget_dict[category][0]
        break

if not date_exists:
    new_row = {'Date': f'{month} {year}'}
    for category in categories:
        new_row[category] = budget_dict[category][0]
    df = df.append(new_row, ignore_index=True)

else:
    new_row = {'Date': f'{month} {year}'}
    for category in categories:
        new_row[category] = budget_dict[category][0]
    df = df.append(new_row, ignore_index=True)

# save the updated dataframe to csv file
for i in range(1, len(categories)):
    df = df.rename(columns={f'Spent.{i-1}': categories[i]})
df.to_csv('budget.csv', index=False)

