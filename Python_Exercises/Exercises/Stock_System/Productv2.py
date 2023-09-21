class Productv2:
    # name: None
    # price: None
    # quantity: None

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display(self):
        print("\n*** PRODUCT ***")
        print('Name:', self.name, '\nPrice:', self.price, '\nQuantity:', self.quantity)

    def calculate_total(self, sum):
        sum = self.price*self.quantity
        return sum


class Electronics(Productv2):
    brand: None

    def __init__(self, brand, name, price, quantity):
        super().__init__(name, price, quantity) 
        self.brand = brand
        # print("Brand:", self.brand)

    def display(self):
        super().display()
        print("brand:", self.brand)

class Clothing(Productv2):
    size: None

    def __init__(self, size, name, price, quantity):
        super().__init__(name, price, quantity) 
        self.size = size
        # print("Size:", self.size)

    def display(self):
        super().display()
        print("size:", self.size)


class Books(Productv2):
    author: None

    def __init__(self, author, name, price, quantity):
        super().__init__(name, price, quantity) 
        self.author = author
        # print("Author:", self.author)

    def display(self):
        super().display()
        print("author:", self.author)

