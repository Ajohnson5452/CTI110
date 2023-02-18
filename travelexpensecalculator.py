#This program was created to calculate and display travel expenses.
#2/16/2023
# CTI-110 P1HW2 - Travel Expense
# Andrew Johnson
#Destination User Input
user_destination = (input("Enter travel destination: "))
#Trip Budget User Input
user_budget = int(input("Enter your Budget: $"))
#Fuel User Input
gas_budget = int(input("How much do you think you will spend on gas? $"))
# Accommodation User Input
lodging_budget = int(input("Approxiamately, how much will you will need for accommodation? $"))
# Food User Input
food_budget = int(input("How much do you need for food? $"))
#Travel Details
print("-----------Travel Summary---------------")
print(f"Location: {user_destination}")
print(f"Initial Budget: ${user_budget}")
#Projected Expenses
print(f"Fuel: ${gas_budget}")
print(f"Accommodation: ${lodging_budget}")
print(f"Food: ${food_budget}")
#Total Expenses  formula
user_expenses = gas_budget + lodging_budget + food_budget
print("--------------------------------")
print(f"Total Expenses:  ${user_expenses} ")
#Results
#Remaining Balance formula
budgetminusexpenses = user_budget - user_expenses
#Remaining Balance
print("--------------------------------")
print(f"Remaining Balance: ${budgetminusexpenses}")