import function as ft

def main():
    user_file = 'user.csv'

    user_id = input("Enter your User ID: ")
    user_ic = input("Enter your IC number: ")
    password = input("Enter the last 4 digits of your IC as password: ")
    user_status = input("Are you a new user? (Y/N): ").strip().upper()

    while user_status == 'Y':
        if not ft.register_user(user_id, user_ic, user_file):
            print("Registration failed. Please try again.")
            user_id = input("Enter your User ID: ")
            user_ic = input("Enter your IC number: ")
            password = input("Enter the last 4 digits of your IC as password: ")
            user_status = input("Are you a new user? (Y/N): ").strip().upper()
            continue
        print("Registration successful. Please log in again.")
        user_status = 'N'  # Change status to allow login after registration
        user_id = input("Enter your User ID: ")
        user_ic = input("Enter your IC number: ")
        password = input("Enter the last 4 digits of your IC as password: ")

    while user_status == 'N':
        if ft.ic_checking(user_ic, user_file):
            if ft.verify_user(user_ic, password):
                income = float(input("Enter your annual income: "))
                tax_relief = ft.calculate_tax_relief()

                tax_payable = ft.calculate_tax(income, tax_relief)
                print(f"Your tax payable is {tax_payable}")

                data = {
                    'User ID': user_id, 
                    'IC Number': user_ic, 
                    'Income': income, 
                    'Tax Relief': tax_relief, 
                    'Tax Payable': tax_payable
                }
                ft.save_to_csv(data, user_file)
                break
            else:
                print("Invalid credentials. Please try again.")
                user_id = input("Enter your User ID: ")
                user_ic = input("Enter your IC number: ")
                password = input("Enter the last 4 digits of your IC as password: ")
        else:
            print("IC number not registered. Please register first.")
            user_status = 'Y'  # Change status to allow registration
            user_id = input("Enter your User ID: ")
            user_ic = input("Enter your IC number: ")
            password = input("Enter the last 4 digits of your IC as password: ")

if __name__ == "__main__":
    main()
