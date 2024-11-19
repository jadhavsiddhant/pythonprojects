users = {'user1': {'pin': '1234', 'balance': 1000}}

def sign_in():
    username = input("Enter Username: ")
    if username in users:
        pin = input("Enter PIN: ")
        if users[username]['pin'] == pin:
            print("Sign In Successful!")
            return username
        else:
            print("Invalid PIN.")
    else:
        print("User not found.")
    return None

def withdraw(username):
    amount = float(input("Enter amount to withdraw: "))
    if amount <= users[username]['balance']:
        users[username]['balance'] -= amount
        print(f"Withdraw successful! Remaining Balance: {users[username]['balance']}")
    else:
        print("Insufficient balance.")

def deposit(username):
    amount = float(input("Enter amount to deposit: "))
    users[username]['balance'] += amount
    print(f"Deposit successful! New Balance: {users[username]['balance']}")

def change_pin(username):
    new_pin = input("Enter new PIN: ")
    users[username]['pin'] = new_pin
    print("PIN changed successfully.")

while True:
    print("\nATM Simulator")
    print("1. Sign In")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        user = sign_in()
        if user:
            while True:
                print("\n1. Withdraw")
                print("2. Deposit")
                print("3. Change PIN")
                print("4. Sign Out")
                sub_choice = input("Enter your choice: ")

                if sub_choice == '1':
                    withdraw(user)
                elif sub_choice == '2':
                    deposit(user)
                elif sub_choice == '3':
                    change_pin(user)
                elif sub_choice == '4':
                    print("Signing Out...")
                    break
                else:
                    print("Invalid choice, please try again.")
    elif choice == '2':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")
