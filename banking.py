from this import d


# Parent class
class User():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def show_details(self):
        print("Personal details")
        print("")
        print("Name",self.name)
        print("Age",self.age)
        print("Gander",self.gender)

# Child Class it takes all the char from the parent class.
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender) 

        self.balance = 0

    def deposit(self,amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Amount balance has been updated:", self.balance) 

    def withdraw(self,amount):
        self.amount = amount
        if self.amount > self.balance:
            print("No enough funds:: Abalance avialible is:", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Account balance has been updated:", self.balance)

    def view_balance(self):
        self.show_details()
        print("Account balance:", self.balance)      