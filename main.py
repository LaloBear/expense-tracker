import expense_utils

expenses = expense_utils.load_expenses()

while True:
    print("1. Add expense")
    print("2. View expense")
    print("3. View total cost")
    print("4. Delete expense")
    print("5. View by category")
    print("6. View total by category")
    print("7. Search by date")
    print("8. Edit expense")
    print("9. Sort by cost")
    print("10. Exit")
    try:
        choice = int(input("Choice:"))
    except:
        print("Invalid choice.\n")
        continue

    if choice == 1:
        if expense_utils.add_expense(expenses):
            expense_utils.save_expenses(expenses)

    elif choice == 2:
        expense_utils.view_expense(expenses)

    elif choice == 3:
        expense_utils.view_total(expenses)

    elif choice == 4:
        if expense_utils.delete_expense(expenses):
            expense_utils.save_expenses(expenses)

    elif choice == 5:
        expense_utils.search_by_category(expenses)

    elif choice == 6:
        expense_utils.total_by_category(expenses)

    elif choice == 7:
        expense_utils.search_by_date(expenses)

    elif choice == 8:
        if expense_utils.edit_expenses(expenses):
            expense_utils.save_expenses(expenses)

    elif choice == 9:
        expense_utils.sort_by_cost(expenses)

    elif choice == 10:
        print("Exiting")
        break

    else:
        print("Invalid response.\n")