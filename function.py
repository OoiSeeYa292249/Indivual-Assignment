import csv
import pandas as pd
import os

def verify_user(user_ic, password):
    if len(user_ic) == 12 and (password == user_ic[-4:]):
        return True
    else:
        print("Please check your IC and password again.")
        return False

def ic_checking(user_ic, user_file):
    try:
        if os.path.isfile(user_file):
            df = pd.read_csv(user_file, dtype={'User IC': str, 'Password': str})
            return user_ic in df['User IC'].values    
        else:
            print("User file does not exist.")
            return False
    except Exception as e:
        print(f"Error checking IC: {e}")
        return False

def save_to_csv(data, user_file):
    df = pd.DataFrame([data])
    header = not os.path.isfile(user_file)
    try: 
        df.to_csv(user_file, mode='a', header=header, index=False)
    except Exception as e:
        print(f"Failed to save to csv: {e}")

def read_from_csv(user_file):
    try:
        if os.path.isfile(user_file):
            df = pd.read_csv(user_file, dtype={'User IC': str, 'Password': str})
            return df
        else:
            print("User file does not exist.")
            return None
    except Exception as e:
        print(f"Error reading from CSV: {e}")
        return None

def get_user_ic(user_id, password):
    try:
        df = pd.read_csv('users.csv', dtype={'User IC': str, 'Password': str})
        user = df[(df['User ID'] == user_id) & (df['Password'] == password)]
        if not user.empty:
            return user['User IC'].values[0]
        else:
            print("User not found or incorrect password.")
            return None
    except Exception as e:
        print(f"Error retrieving user IC: {e}")
        return None

def calculate_tax_relief():
    tax_relief = 9000

    married = input("Are you married? (Y/N): ").strip().upper()
    if married == 'Y':
        spouse_income = float(input("Enter your spouse's income: "))
        if spouse_income <= 4000:
            tax_relief += 4000

    children = int(input("How many children do you have? (Maximum: 12): "))
    tax_relief += min(children, 12) * 8000

    medical_expenses = float(input("Enter your medical expenses: "))
    tax_relief += min(medical_expenses, 8000)

    lifestyle_expenses = float(input("Enter your lifestyle expenses: "))
    tax_relief += min(lifestyle_expenses, 2500)

    education_expenses = float(input("Enter your education expenses: "))
    tax_relief += min(education_expenses, 7000)

    parental_care = float(input("Enter your parental care expenses: "))
    tax_relief += min(parental_care, 5000)

    return tax_relief

def calculate_tax(income, tax_relief):
    taxable_income = max(0, income - tax_relief)
    if taxable_income <= 5000:
        tax_payable = 0
    elif taxable_income <= 20000:
        tax_payable = (taxable_income - 5000) * 0.1
    elif taxable_income <= 35000:
        tax_payable = 1500 + (taxable_income - 20000) * 0.15
    elif taxable_income <= 50000:
        tax_payable = 3750 + (taxable_income - 35000) * 0.2
    else:
        tax_payable = 6750 + (taxable_income - 50000) * 0.25
    
    return tax_payable

def register_user(user_id, user_ic, user_file):
    try:
        if not os.path.isfile(user_file):
            df = pd.DataFrame(columns=['User ID', 'User IC', 'Password'])
        else:
            df = pd.read_csv(user_file, dtype={'User IC': str, 'Password': str})

        if user_ic in df['User IC'].values:
            print("IC number already registered.")
            return False

        password = user_ic[-4:]
        new_user = {'User ID': user_id, 'User IC': user_ic, 'Password': password}
        df = df.append(new_user, ignore_index=True)

        save_to_csv(new_user, user_file)
        print("User registered successfully.")
        return True
    except Exception as e:
        print(f"Error registering user: {e}")
        return False
