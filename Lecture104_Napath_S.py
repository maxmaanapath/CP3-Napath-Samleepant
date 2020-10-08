class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added to ",self.name,self.lastName,"'s cart")

customer1 = Customer()
customer1.name = "Napath"
customer1.lastName = "S"
customer1.addCart()

customer2 = Customer()
customer2.name = "Papassorn"
customer2.lastName = "K"
customer2.addCart()

customer3 = Customer()
customer3.name = "Anusara"
customer3.lastName = "G"
customer3.addCart()

customer4 = Customer()
customer4.name = "Narong"
customer4.lastName = "S"
customer4.addCart()