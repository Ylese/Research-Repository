# class Product():
#     name: None
#     price: None
#     quantity: None

#     def __init__(self, name, quantity):
#         self.name = name
#         self.price = 0.00
#         self.quantity = quantity

#     def display(self):
#         print("Name:", self.name)
#         print("Price:", self.price)
#         print("Quantity:", self.quantity)
    
#     def get_price(self, sum):
#         self.price += sum
    
#     def set_price(self, sum):
#         self.price +=sum
    
#     def get_quantity(self, sum):
        

# product = Product("Tiramisu", "10")
# product.get_price(10)
# product.display()

class Product():
    def __init__(self, name, quantity):
        self.name = name
        self.price = 0.00
        self.quantity = 0

    def display(self):
        print("\n\033[96m^^^^^^\tWelcome to Huie's Cafe!\t^^^^^^\033[0m\n\n\033[104m Menu \033[0m \n")
        print("Product Name:", self.name, "\nPrice:", self.price, '\nQuantity:', self.quantity)

    
    def get_price(self, sum):
        self.price += sum
    
    def set_price(self, sum):
        self.price += sum
    
    def get_quantity(self, sum):
        self.quantity += sum
    
    def set_quantity(self, sum):
        self.quantity += sum
    
    def sell(self, sum):
        if sum <= self.quantity:
            self.quantity -= sum 
    
    def cost(self, sum):
        self.price == sum*self.price


product = Product("Tiramisu", "10")
product.get_price(95)
product.set_price(25)
product.get_quantity(11)
product.set_price(20)
product.sell(9)
product.cost(1)
product.display()