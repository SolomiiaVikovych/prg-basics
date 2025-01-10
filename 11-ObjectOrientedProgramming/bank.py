class Card:
    def __init__(self,number):
        self.balance = 0
        self.number = number

    def deposit(self,emount):
        self.balance += emount
    def withdraw(self,emount):
        if emount <= self.balance:
            self.balance -= emount
        else:
            print("Insufficient funds on the account")

    def show_info(self):
        print(f'Bank account: {self.number}')
        print(f'Balance: {self.balance}')
        

        