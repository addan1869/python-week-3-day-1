class Bank:

    def deposit(self):
        self.amount = int(input("Enter Deposit Amount: "))
        print("Amount Deposited:", self.amount)

b1 = Bank()
b1.deposit()