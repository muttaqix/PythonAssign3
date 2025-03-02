from person import Person

def main():
    name = input("Enter your name: ")
    acct_type = input("Choose account type (Chequing/Savings): ")
    user = Person(name, acct_type)

    while True:
        task = input("Choose an action (deposit/withdraw/exit): ")
        if task == "deposit":
            amount = float(input("Enter deposit amount: "))
            user.deposit(amount)
        elif task == "withdraw":
            amount = float(input("Enter withdrawal amount: "))
            user.withdraw(amount)
        elif task == "exit":
            print("Exiting")
            break
        else:
            print("Invalid. Please try again.")

if __name__ == "__main__":
    main()    