from Productv2 import Productv2, Electronics, Clothing, Books

if __name__ == "__main__":
    item1 = Productv2("Tiramisu", 50.00, 5)
    item1.display()
    item1.calculate_total(5)

    item2 = Electronics("Apple", "Iphone 14 Pro Max", 4000.00, 2)
    item2.display()

    item3 = Clothing(10, "Pants", 50.00, 5)
    item3.display()

    item4 = Books("Colleen Hoover", "Collided", 45.00, 10)
    item4.display()