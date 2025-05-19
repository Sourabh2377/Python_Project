import random  #used to generate random numbers

class BankAccount:
    existing_account_numbers = set()

    def __init__(self, name, balance=0):
        self.name = name
        self.__balance = balance
        self.account_number = self.generate_account_number()
        BankAccount.existing_account_numbers.add(self.account_number)

    def generate_account_number(self):
        while True:
            acc_num = random.randint(10000000, 99999999)  # 8-digit random number
            if acc_num not in BankAccount.existing_account_numbers:
                return acc_num

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"✅ Deposited ₹{amount}. New balance: ₹{self.__balance}")
        else:
            print("❌ Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"✅ Withdrew ₹{amount}. New balance: ₹{self.__balance}")
        else:
            print("❌ Insufficient balance.")

    def check_balance(self):
        print(f"\n👤 Account Holder: {self.name}")
        print(f"🏦 Account Number: {self.account_number}")
        print(f"💰 Current Balance: ₹{self.__balance}\n")


def find_account(accounts, acc_number):
    for account in accounts:
        if account.account_number == acc_number:
            return account
    return None


def main():
    print("🏦 Welcome to Python Bank")

    accounts = []

    while True:
        print("\n1. Create New Account")
        print("2. Access Existing Account")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter your name: ")
            account = BankAccount(name)
            accounts.append(account)
            print(f"\n✅ Account created successfully!")
            print(f"👤 Name: {account.name}")
            print(f"🏦 Account Number: {account.account_number}")

        elif choice == "2":
            try:
                acc_number = int(input("Enter your account number: "))
                account = find_account(accounts, acc_number)
                if account:
                    print(f"\nWelcome back, {account.name}!")
                    while True:
                        print("\n--- Menu ---")
                        print("1. Deposit")
                        print("2. Withdraw")
                        print("3. Check Balance")
                        print("4. Logout")
                        sub_choice = input("Choose an option: ")

                        if sub_choice == "1":
                            amount = float(input("Enter amount to deposit: ₹"))
                            account.deposit(amount)
                        elif sub_choice == "2":
                            amount = float(input("Enter amount to withdraw: ₹"))
                            account.withdraw(amount)
                        elif sub_choice == "3":
                            account.check_balance()
                        elif sub_choice == "4":
                            print("Logging out...")
                            break
                        else:
                            print("❌ Invalid option. Try again.")
                else:
                    print("❌ Account number not found.")
            except ValueError:
                print("❌ Invalid input. Please enter a valid account number.")

        elif choice == "3":
            print("👋 Thank you for banking with us!")
            break
        else:
            print("❌ Invalid option. Try again.")


if __name__ == "__main__":
    main()
