Expenses = [] #list of all expenses

print("Welcome to the Expense Tracker!: Save moeney and track your expenses with us!")

while True:
    print("====Menu====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View total expenses")
    print("4. Exit")

    choice = input("Please enter your choice: ")

    #1. Add Expense
    if choice == '1':
        date = input("Enter the date of the expense (YYYY-MM-DD): ")
        category = input("Enter the category of the expense(food,travel,shopping etc): ")
        description = input("Enter a description for the expense: ")
        amount = float(input("Enter the amount of the expense: "))
        
        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }
        
        Expenses.append(expense)
    #2. View All Expenses
    elif choice == '2':
        
        for expense in Expenses:
            print(f"Date: {expense['date']}, Category: {expense['category']}, Description: {expense['description']}, Amount: {expense['amount']}")
    
    #3. View total expenses
    elif choice == '3':
        total = sum(expense['amount'] for expense in Expenses)
        print(f"Total expenses: {total}")
    
    #4. Exit
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
