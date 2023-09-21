#Product class
class Product():
    # product_id: None
    # name: None
    # price: None
    # quantity: None
    # __status: None

    #constructor
    def __init__(self, product_id, name, price, quantity, status = True):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.__status = status #private

    #display
    def display(self):
        print("*** PRODUCT ***")
        print("ID:", self.product_id)
        print("Name:", self.name)
        print("Price: $", self.price)
        print("Quantity:", self.quantity)
        if self.__status:
            print("ACTIVE")
        else:
            print("ARCHIVE")

    #cost calculation
    def cost(self):
        return self.price * self.quantity
    
    #getter
    def get_status(self):
        return self.__status
    
    #setter
    def set_status(self, new_value):
        self.__status = new_value



# test
p1 = Product(2001, "Peanut cookies", 5.99, 12)
p1.display()
# print(p1.__status) #error

#test2
print("Total Cost = $", p1.cost())

#test3
print("is active?", p1.get_status())

# #test4
# p1.set_status(False)
# p1.display()