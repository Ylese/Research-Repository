from Product1 import *
class StockSystem:
    product_list = []
    last_id = 2000

    #constructor
    def __init__(self):
        #add some dummie products
        new_product = Product(2001, "Peanut cookies", 5.99, 12, True)
        self.product_list.append(new_product)

        new_product = Product(2002, "Chocolate cookies", 5.99, 10, True)
        self.product_list.append(new_product)
        
        new_product = Product(2003, "Apple pie", 3.20, 20, False)
        self.product_list.append(new_product)

        #increment
        self.next_id = 2004

    #display all products
    def display_all_products(self):
        print("\n*** LIST OF PRODUCTS ***\n")

        if len(self.product_list) == 0:
            print("No Products to Show")
        for p in self.product_list:
            p.display()
    
    #add new product to the system
    def add_new_product(self):

        print("\n***ENTER NEW PRODUCT ***\n")
        #input of name
        name = input("Enter the name of the product:")
        if name == "":
            print("Incorrect input!")
            return
        
        #input of price
        price = input("Enter the price:")
        try:
            price = float(price)
        except:
            print(price, "is an incorrect number.")
            return

        quantity = input("Enter the quantity:")
        try:
            price = int(quantity)
        except:
            print(price, "is an incorrect number.")
            return
        
        #add product to list
        new_product = Product(self.next_id, name, price, quantity)
        self.product_list.append(new_product)
        self.next_id += 1
        



#test1       
ss = StockSystem()
ss.display_all_products()

#test2

ss.add_new_product()
ss.display_all_products()