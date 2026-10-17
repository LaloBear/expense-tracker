import json

def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)

def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except:
        return[]

def add_expense(expenses):
    
    name = input("Expense Name:").strip()

    if name == "":
        print("Name cannot be empty.\n")
        return False

    try:
        cost = float(input("Cost:").strip())
    except:
        print("Invalid cost.\n")
        return False
    
    if cost <= 0:
        print("Cost must be greater than 0.\n")
        return False
    
    category = input("Category:").strip()

    if category == "":
        print("Category cannot be empty.\n")
        return False
    
    date = input("Date:").strip()
    
    if date == "":
        print("Date cannot be empty.\n")
        return False

    expenses.append({"name": name, "cost": cost, "category" : category, "date": date})
    print()
    return True

def view_expense(expenses):
    if not expenses:
        print("Empty try adding an expense.\n")
        return
    
    else:
        for e in expenses:
            print(e["name"], "|", "$" + format(e["cost"], ".2f"), "|", e["category"], "|", e["date"])
        print()

def view_total(expenses):
    if not expenses:
        print("Empty try adding an expense.\n")
        return

    total = 0

    for e in expenses:
        total = e["cost"] + total
    
    print("Total cost:", "$" + format(total, ".2f"))
    print()

def delete_expense(expenses):
    if not expenses:
        print("Empty try adding an expense.\n")
        return False
    
    name = input("Enter expense name:").strip()

    for e in expenses:
        if e["name"].strip().lower() == name.lower():
            confirmation = input("Are you sure you want to delete this expense? (yes/no):").strip().lower()
            
            if confirmation == "yes":
                expenses.remove(e)
                print("Expense deleted.\n")
                return True
            elif confirmation == "no":
                print("Delete cancelled.\n")
                return False
            else:
                print("Invalid input.\n")
                return False
    
    print("Not found.\n")
    return False

def search_by_category(expenses):
    if not expenses:
        print("Empty, try adding an expense.\n")
        return
    
    category = input("Enter category:").strip().lower()

    found = False

    for e in expenses:
        if category == e["category"].lower():
            print(e["name"], "|", "$" + format(e["cost"], ".2f"), "|", e["category"], "|", e["date"])
            found = True
    
    print()
    
    if not found:
        print("No expenses found.\n")

def total_by_category(expenses):
    if not expenses:
        print("Empty, try adding an expense.\n")
        return 
    
    category = input("Enter category:").strip().lower()

    found = False
    total = 0

    for e in expenses:
        if category == e["category"].lower():
            total = total + e["cost"]
            found = True

    if found:
        print("Total for", category + ":", "$" + format(total, ".2f"))
        print()
    
    if not found:
        print("Category not found.\n")

def search_by_date(expenses):

    if not expenses:
        print("Empty, try adding an expense.\n")
        return 
    
    date = input("Enter date:").strip().lower()

    found = False

    for e in expenses:
        if date == e["date"].lower():
            print(e["name"], "|", "$" + format(e["cost"], ".2f"), "|", e["category"], "|", e["date"])
            found = True
    print()

    if not found:
        print("Not found.\n") 

def edit_expenses(expenses):
    if not expenses:
        print("Empty, try adding an expense.\n")
        return False
    
    name = input("Enter name:").strip().lower()

    for e in expenses:
        if name == e["name"].lower():
            new_name = input("Enter new name:").strip()

            if new_name == "":
                print("Name cannot be empty.\n")
                return False

            new_category = input("Enter new category:").strip()

            if new_category == "":
                print("Category cannot be empty.\n")
                return False

            try:
                new_cost = float(input("Enter new cost:").strip())
            except:
                print("Invalid cost.\n")
                return False

            if new_cost <= 0:
                print("Cost must be greater than 0.\n")
                return False
                        
            new_date = input("Enter new date:").strip()
            
            if new_date == "":
                print("Date cannot be empty.\n")
                return False

            e["name"] = new_name
            e["category"] = new_category
            e["cost"] = new_cost
            e["date"] = new_date

            print("Expense updated.\n")
            return True
    
    print("Expense not found.\n")
    return False

def sort_by_cost(expenses):
    if not expenses:
        print("Empty, try adding an expense.\n")
        return 

    sorted_expenses = sorted(expenses, key=lambda e: e["cost"])

    for e in sorted_expenses:
        print(e["name"], "|", "$" + format(e["cost"], ".2f"), "|", e["category"], "|", e["date"])
    print()