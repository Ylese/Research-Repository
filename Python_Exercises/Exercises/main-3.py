from Cat2 import Cat2, DomesticCat, WildCat

if __name__ == "__main__":
    cat1=Cat2("Luna", 5, True )
    cat1.display()
    cat1.sound()

    cat1.isHappy = False
    cat1.display()

    dc = DomesticCat("Huie", "Raven", 5, False)
    dc.display()
    dc.sound()

    wc1 = WildCat('tiger', 10)
    wc1.display()
    wc1.sound()